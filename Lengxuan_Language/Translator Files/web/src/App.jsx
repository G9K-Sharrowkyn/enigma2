import React, { useEffect, useMemo, useRef, useState } from "react";
import { buildPlPhraseIndex, parseTsv } from "./lexicon.js";
import { translateLxToPl, translatePlToLx } from "./translate.js";

function useLexicons() {
  const stateRef = useRef({
    ready: false,
    lx2plMap: null,
    plIndex: null
  });
  const [, force] = useState(0);

  useEffect(() => {
    let cancelled = false;
    async function load() {
      const [pl2lxText, lx2plText] = await Promise.all([
        fetch("/lexicon_pl2lx.tsv").then((r) => r.text()),
        fetch("/lexicon_lx2pl.tsv").then((r) => r.text())
      ]);
      if (cancelled) return;

      const pl2lxMap = parseTsv(pl2lxText);
      const lx2plMap = parseTsv(lx2plText);
      const plIndex = buildPlPhraseIndex(pl2lxMap);

      stateRef.current = { ready: true, lx2plMap, plIndex };
      force((x) => x + 1);
    }
    load();
    return () => {
      cancelled = true;
    };
  }, []);

  return stateRef.current;
}

export default function App() {
  const [direction, setDirection] = useState("pl2lx"); // 'pl2lx' | 'lx2pl'
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [unknown, setUnknown] = useState([]);

  const lex = useLexicons();

  const modeLabel = direction === "pl2lx" ? "PL → Lengxuan" : "Lengxuan → PL";
  const leftLabel = direction === "pl2lx" ? "Polski" : "Lengxuan";
  const rightLabel = direction === "pl2lx" ? "Lengxuan" : "Polski";

  useEffect(() => {
    if (!lex.ready) {
      setOutput("");
      setUnknown([]);
      return;
    }
    if (!input.trim()) {
      setOutput("");
      setUnknown([]);
      return;
    }
    if (direction === "pl2lx") {
      const res = translatePlToLx(input, lex.plIndex);
      setOutput(res.text);
      setUnknown(res.unknown);
    } else {
      const res = translateLxToPl(input, { lx2plMap: lex.lx2plMap });
      setOutput(res.text);
      setUnknown(res.unknown);
    }
  }, [direction, input, lex.ready]);

  const unknownInfo = useMemo(() => {
    const uniq = Array.from(new Set(unknown));
    if (!uniq.length) return null;
    const shown = uniq.slice(0, 8).join(", ");
    const rest = uniq.length > 8 ? ` (+${uniq.length - 8})` : "";
    return `${shown}${rest}`;
  }, [unknown]);

  const swap = () => {
    setDirection((d) => (d === "pl2lx" ? "lx2pl" : "pl2lx"));
    setInput(output);
  };

  const copyOut = async () => {
    try {
      await navigator.clipboard.writeText(output ?? "");
    } catch {
      // ignore
    }
  };

  return (
    <div className="wrap">
      <div className="header">
        <div>
          <h1 className="title">Lengxuan Translator</h1>
          <p className="subtitle">
            Offline, regułowy tłumacz oparty o `03_Slownik/` (słowniki z `Translator Files/out`).
          </p>
        </div>
        <div className="controls">
          <span className="pill">{lex.ready ? "Lexicon: OK" : "Ładowanie słownika..."}</span>
          <button className="btn btnPrimary" onClick={() => setDirection((d) => (d === "pl2lx" ? "lx2pl" : "pl2lx"))}>
            {modeLabel}
          </button>
          <button className="btn" onClick={swap} disabled={!lex.ready}>
            Zamień
          </button>
          <button className="btn" onClick={copyOut} disabled={!output}>
            Kopiuj wynik
          </button>
        </div>
      </div>

      <div className="grid">
        <div className="panel">
          <div className="panelHead">
            <div className="panelTitle">{leftLabel}</div>
            <div className="panelTitle">{unknownInfo ? `Nieznane: ${unknown.length}` : " "}</div>
          </div>
          <textarea
            placeholder={direction === "pl2lx" ? "Wpisz tekst po polsku..." : "Wpisz tekst w Lengxuan..."}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            spellCheck={direction === "pl2lx"}
          />
        </div>

        <div className="panel">
          <div className="panelHead">
            <div className="panelTitle">{rightLabel}</div>
            <div className="panelTitle">{unknownInfo ? `(${unknownInfo})` : " "}</div>
          </div>
          <textarea value={output} readOnly placeholder={lex.ready ? "Tłumaczenie pojawi się tutaj..." : "Ładowanie..."} />
        </div>
      </div>

      <div className="footer">
        To jest wersja „prosta”: tłumaczenie = słownik + tokenizacja + dopasowanie fraz (najdłuższe dopasowanie), bez pełnej
        składni ani odmiany.
      </div>
    </div>
  );
}

