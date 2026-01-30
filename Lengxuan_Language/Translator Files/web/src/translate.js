import { aliasLx, joinTokens, splitTokens } from "./lexicon.js";

const PUNCT = new Set([".", ",", "!", "?", ";", ":", "(", ")", "\""]);

const DROP_PL = new Set(["do", "w", "we", "na", "za", "o", "że", "żeby", "się"]);
const PRON_CASES = new Map([
  ["mnie", "ja"],
  ["mi", "ja"],
  ["mną", "ja"],
  ["ciebie", "ty"],
  ["cię", "ty"],
  ["ci", "ty"],
  ["tobie", "ty"],
  ["jego", "on/ona"],
  ["go", "on/ona"],
  ["jemu", "on/ona"],
  ["jej", "on/ona"],
  ["ją", "on/ona"],
  ["niej", "on/ona"],
  ["nim", "on/ona"],
  ["nią", "on/ona"]
]);

export function translatePlToLx(text, { phraseMap, maxLen }) {
  const tokens = splitTokens(text);
  const out = [];
  const unknown = [];

  let i = 0;
  while (i < tokens.length) {
    const tok = tokens[i];
    if (PUNCT.has(tok)) {
      out.push(tok);
      i += 1;
      continue;
    }

    if (tok === "nie" && i + 1 < tokens.length && !PUNCT.has(tokens[i + 1])) {
      out.push("daoo");
      i += 1;
      continue;
    }

    let matched = false;
    const spanMax = Math.min(maxLen, tokens.length - i);
    for (let l = spanMax; l >= 1; l--) {
      const key = tokens.slice(i, i + l).join(" ");
      const cand = phraseMap.get(key);
      if (cand?.length) {
        out.push(cand[0]);
        i += l;
        matched = true;
        break;
      }
    }
    if (matched) continue;

    // aliasy proste (przypadki zaimków)
    const alias = PRON_CASES.get(tok);
    if (alias) {
      const cand = phraseMap.get(alias);
      if (cand?.length) out.push(cand[0]);
      else out.push(`[[${tok}]]`);
      i += 1;
      continue;
    }

    if (DROP_PL.has(tok)) {
      i += 1;
      continue;
    }

    unknown.push(tok);
    out.push(`[[${tok}]]`);
    i += 1;
  }

  return { text: joinTokens(out, { capitalizeFirst: false }), unknown };
}

export function translateLxToPl(text, { lx2plMap }) {
  const tokens = splitTokens(text);
  const out = [];
  const unknown = [];

  let question = false;
  if (tokens.length && tokens[tokens.length - 1] === "mo") {
    tokens.pop();
    question = true;
  }

  for (const tok of tokens) {
    if (PUNCT.has(tok)) {
      out.push(tok);
      continue;
    }
    const cand = lx2plMap.get(tok) ?? lx2plMap.get(aliasLx(tok));
    if (!cand?.length) {
      unknown.push(tok);
      out.push(`[[${tok}]]`);
    } else {
      out.push(cand[0]);
    }
  }

  if (question) out.push("?");
  return { text: joinTokens(out, { capitalizeFirst: true }), unknown };
}

