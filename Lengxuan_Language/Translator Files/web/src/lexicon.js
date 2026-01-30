const PUNCT_RE = /([.,!?;:()"'“”])/g;
const SPACE_RE = /\s+/g;

export function normalize(text) {
  return (text ?? "")
    .trim()
    .replaceAll("„", "\"")
    .replaceAll("”", "\"")
    .replaceAll("“", "\"")
    .replace(PUNCT_RE, " $1 ")
    .replace(SPACE_RE, " ")
    .trim()
    .toLowerCase();
}

export function splitTokens(text) {
  const norm = normalize(text);
  return norm ? norm.split(" ") : [];
}

export function parseTsv(text) {
  const map = new Map();
  const lines = (text ?? "").split(/\r?\n/);
  for (const line of lines) {
    if (!line || line.startsWith("#")) continue;
    const [a, b] = line.split("\t");
    if (!a || !b) continue;
    const key = a.trim();
    const val = b.trim();
    if (!map.has(key)) map.set(key, []);
    const arr = map.get(key);
    if (!arr.includes(val)) arr.push(val);
  }
  return map;
}

export function buildPlPhraseIndex(pl2lxMap) {
  const phraseMap = new Map();
  let maxLen = 1;
  for (const [pl, lxs] of pl2lxMap.entries()) {
    const key = normalize(pl);
    if (!key) continue;
    const toks = key.split(" ");
    maxLen = Math.max(maxLen, toks.length);
    const phraseKey = toks.join(" ");
    if (!phraseMap.has(phraseKey)) phraseMap.set(phraseKey, []);
    const arr = phraseMap.get(phraseKey);
    for (const lx of lxs) {
      if (!arr.includes(lx)) arr.push(lx);
    }
  }
  return { phraseMap, maxLen };
}

export function aliasLx(token) {
  return token.replaceAll("ǎ", "a").replaceAll("ǒ", "o");
}

export function joinTokens(tokens, { capitalizeFirst = false } = {}) {
  const out = [];
  for (const t of tokens) {
    if ([".", ",", "!", "?", ";", ":", ")"].includes(t)) {
      if (out.length) out[out.length - 1] = out[out.length - 1] + t;
      else out.push(t);
      continue;
    }
    if (["(", "\""].includes(t)) {
      out.push(t);
      continue;
    }
    if (out.length && out[out.length - 1] === "\"") out[out.length - 1] = out[out.length - 1] + t;
    else out.push(t);
  }
  let s = out.join(" ").replaceAll("\" ", "\"").replaceAll(" \"", "\"").trim();
  if (capitalizeFirst && s) s = s[0].toUpperCase() + s.slice(1);
  return s;
}

