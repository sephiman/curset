import { useTranslation } from "react-i18next";
import type { ResolvedTheme } from "@/lib/theme";

/**
 * Two-panel SVG illustrating order book depth and market order slippage (m02).
 * Left: Order book depth ladder (Asks, Spread, Bids).
 * Right: Step-by-step market buy execution through resting ask tiers.
 */
export function OrderBookDepth({ theme }: { theme?: ResolvedTheme } = {}) {
  const { t, i18n } = useTranslation();
  const light = theme === "light";
  const isEs = (i18n.resolvedLanguage || "en").startsWith("es");

  // Format helper for numbers in diagram
  const p200 = isEs ? "2,00" : "2.00";
  const p202 = isEs ? "2,02" : "2.02";
  const p205 = isEs ? "2,05" : "2.05";
  const p198 = isEs ? "1,98" : "1.98";
  const p196 = isEs ? "1,96" : "1.96";
  const p194 = isEs ? "1,94" : "1.94";

  const q500 = isEs ? "500 u." : "500 u";
  const q800 = isEs ? "800 u." : "800 u";
  const q1500 = isEs ? "1.500 u." : "1,500 u";
  const q600 = isEs ? "600 u." : "600 u";
  const q1000 = isEs ? "1.000 u." : "1,000 u";
  const q1200 = isEs ? "1.200 u." : "1,200 u";

  // Palette styles: default classes are light mode; dark:/oled: handle dark modes.
  // When pinned to light (PDF export), dark classes are omitted.
  const cardBg = light
    ? "fill-white stroke-gray-200"
    : "fill-white dark:fill-gray-900 stroke-gray-200 dark:stroke-gray-800 oled:fill-black oled:stroke-gray-850";

  const cardInner = light
    ? "fill-gray-50 stroke-gray-200"
    : "fill-gray-50 dark:fill-gray-800/70 stroke-gray-200 dark:stroke-gray-700/80 oled:fill-gray-950";

  const calloutBg = light
    ? "fill-amber-50 stroke-amber-300"
    : "fill-amber-50 dark:fill-amber-950/40 stroke-amber-300 dark:stroke-amber-700/70 oled:fill-amber-950/20";

  const textTitle = light
    ? "fill-gray-900 font-semibold"
    : "fill-gray-900 dark:fill-gray-100 font-semibold";

  const textMuted = light
    ? "fill-gray-600 text-[10px]"
    : "fill-gray-600 dark:fill-gray-400 text-[10px]";

  const textQty = light
    ? "fill-gray-900 font-mono text-[10.5px] font-medium"
    : "fill-gray-900 dark:fill-gray-200 font-mono text-[10.5px] font-medium";

  const textPriceAsk = light
    ? "fill-rose-700 font-mono text-[11px] font-bold"
    : "fill-rose-700 dark:fill-rose-400 font-mono text-[11px] font-bold";

  const textPriceBid = light
    ? "fill-emerald-700 font-mono text-[11px] font-bold"
    : "fill-emerald-700 dark:fill-emerald-400 font-mono text-[11px] font-bold";

  const barAsk = light ? "fill-rose-100/70" : "fill-rose-100/70 dark:fill-rose-950/50";
  const barAskFilled = light ? "fill-rose-200" : "fill-rose-200 dark:fill-rose-900/60";
  const barBid = light ? "fill-emerald-100/70" : "fill-emerald-100/70 dark:fill-emerald-950/50";

  const divider = light
    ? "stroke-gray-200"
    : "stroke-gray-200 dark:stroke-gray-700/80";

  const pillSpread = light
    ? "fill-gray-100 stroke-gray-300"
    : "fill-gray-100 dark:fill-gray-800 stroke-gray-300 dark:stroke-gray-700 oled:fill-gray-900";

  const textSpread = light
    ? "fill-gray-700 font-sans text-[9.5px] font-semibold"
    : "fill-gray-700 dark:fill-gray-200 font-sans text-[9.5px] font-semibold";

  const textFillStep = light
    ? "fill-gray-900 font-mono text-[10px] font-medium"
    : "fill-gray-900 dark:fill-gray-100 font-mono text-[10px] font-medium";

  return (
    <svg viewBox="0 0 560 260" className="mx-auto h-auto w-full max-w-2xl" role="img">
      {/* ------------------------------------------------------------- */}
      {/* LEFT PANEL: Order Book Ladder                                */}
      {/* ------------------------------------------------------------- */}
      <rect x={10} y={10} width={260} height={240} rx={8} className={cardBg} strokeWidth={1} />

      {/* Header */}
      <text x={24} y={30} className={`${textTitle} text-[11.5px]`}>
        {t("orderbook.title_depth")}
      </text>
      <text
        x={256}
        y={30}
        textAnchor="end"
        className={light ? "fill-rose-700 font-sans text-[9.5px] font-semibold" : "fill-rose-700 dark:fill-rose-400 font-sans text-[9.5px] font-semibold"}
      >
        {t("orderbook.asks")}
      </text>

      {/* Column labels */}
      <text x={24} y={46} className={`${textMuted} font-medium`}>
        {t("orderbook.col_price")}
      </text>
      <text x={256} y={46} textAnchor="end" className={`${textMuted} font-medium`}>
        {t("orderbook.col_size")}
      </text>
      <line x1={20} y1={52} x2={260} y2={52} className={divider} strokeWidth={1} />

      {/* ASKS (Ventas) */}
      {/* Tier 3: 2.05 (1500 u total, 700 filled) */}
      <rect x={120} y={58} width={136} height={18} rx={2} className={barAsk} />
      <rect x={184} y={58} width={72} height={18} rx={2} className={barAskFilled} />
      <text x={24} y={71} className={textPriceAsk}>{p205}</text>
      <text
        x={58}
        y={71}
        className={light ? "fill-rose-700/80 font-sans text-[9px]" : "fill-rose-700/80 dark:fill-rose-400/80 font-sans text-[9px]"}
      >
        {isEs ? "(700 u. fill)" : "(700 u fill)"}
      </text>
      <text x={252} y={71} textAnchor="end" className={textQty}>
        {q1500}
      </text>

      {/* Tier 2: 2.02 (800 u - all filled) */}
      <rect x={176} y={80} width={80} height={18} rx={2} className={barAskFilled} />
      <text x={24} y={93} className={textPriceAsk}>{p202}</text>
      <text x={252} y={93} textAnchor="end" className={textQty}>
        {q800}
      </text>

      {/* Tier 1: 2.00 (500 u - best ask, all filled) */}
      <rect x={206} y={102} width={50} height={18} rx={2} className={barAskFilled} />
      <text x={24} y={115} className={textPriceAsk}>{p200}</text>
      <text
        x={58}
        y={115}
        className={light ? "fill-rose-700 font-sans text-[9px] font-medium" : "fill-rose-700 dark:fill-rose-400 font-sans text-[9px] font-medium"}
      >
        ({t("orderbook.best_ask")})
      </text>
      <text x={252} y={115} textAnchor="end" className={textQty}>
        {q500}
      </text>

      {/* Spread Bar */}
      <line x1={20} y1={130} x2={260} y2={130} strokeDasharray="3 3" className={divider} strokeWidth={1} />
      <rect x={55} y={122} width={170} height={16} rx={8} className={pillSpread} strokeWidth={1} />
      <text x={140} y={133} textAnchor="middle" className={textSpread}>
        {t("orderbook.spread")}
      </text>

      {/* BIDS (Compras) */}
      {/* Tier 1: 1.98 (600 u - best bid) */}
      <rect x={196} y={144} width={60} height={18} rx={2} className={barBid} />
      <text x={24} y={157} className={textPriceBid}>{p198}</text>
      <text
        x={58}
        y={157}
        className={light ? "fill-emerald-700 font-sans text-[9px] font-medium" : "fill-emerald-700 dark:fill-emerald-400 font-sans text-[9px] font-medium"}
      >
        ({t("orderbook.best_bid")})
      </text>
      <text x={252} y={157} textAnchor="end" className={textQty}>
        {q600}
      </text>

      {/* Tier 2: 1.96 (1000 u) */}
      <rect x={156} y={166} width={100} height={18} rx={2} className={barBid} />
      <text x={24} y={179} className={textPriceBid}>{p196}</text>
      <text x={252} y={179} textAnchor="end" className={textQty}>
        {q1000}
      </text>

      {/* Tier 3: 1.94 (1200 u) */}
      <rect x={136} y={188} width={120} height={18} rx={2} className={barBid} />
      <text x={24} y={201} className={textPriceBid}>{p194}</text>
      <text x={252} y={201} textAnchor="end" className={textQty}>
        {q1200}
      </text>

      {/* Bids badge & footer caption */}
      <text
        x={140}
        y={223}
        textAnchor="middle"
        className={light ? "fill-emerald-700 font-sans text-[9.5px] font-semibold" : "fill-emerald-700 dark:fill-emerald-400 font-sans text-[9.5px] font-semibold"}
      >
        {t("orderbook.bids")}
      </text>
      <text
        x={140}
        y={238}
        textAnchor="middle"
        className={light ? "fill-gray-500 font-sans text-[9px]" : "fill-gray-500 dark:fill-gray-400 font-sans text-[9px]"}
      >
        {isEs ? "Barras = liquidez en reposo" : "Bars = resting liquidity"}
      </text>

      {/* ------------------------------------------------------------- */}
      {/* RIGHT PANEL: Execution & Slippage Breakdown                  */}
      {/* ------------------------------------------------------------- */}
      <rect x={285} y={10} width={265} height={240} rx={8} className={cardBg} strokeWidth={1} />

      {/* Header */}
      <text
        x={300}
        y={30}
        className={light ? "fill-amber-700 font-sans text-[11px] font-bold" : "fill-amber-700 dark:fill-amber-400 font-sans text-[11px] font-bold"}
      >
        {t("orderbook.market_buy")}
      </text>
      <text x={300} y={45} className={`${textMuted} font-medium`}>
        {t("orderbook.execution_walk")}
      </text>
      <line x1={295} y1={52} x2={540} y2={52} className={divider} strokeWidth={1} />

      {/* Tier 1 fill card */}
      <rect x={298} y={58} width={238} height={24} rx={4} className={cardInner} strokeWidth={1} />
      <circle cx={310} cy={70} r={3} className={light ? "fill-amber-600" : "fill-amber-600 dark:fill-amber-400"} />
      <text x={320} y={74} className={textFillStep}>
        {t("orderbook.tier1_fill")}
      </text>

      {/* Tier 2 fill card */}
      <rect x={298} y={87} width={238} height={24} rx={4} className={cardInner} strokeWidth={1} />
      <circle cx={310} cy={99} r={3} className={light ? "fill-amber-600" : "fill-amber-600 dark:fill-amber-400"} />
      <text x={320} y={103} className={textFillStep}>
        {t("orderbook.tier2_fill")}
      </text>

      {/* Tier 3 fill card */}
      <rect x={298} y={116} width={238} height={24} rx={4} className={cardInner} strokeWidth={1} />
      <circle cx={310} cy={128} r={3} className={light ? "fill-amber-600" : "fill-amber-600 dark:fill-amber-400"} />
      <text x={320} y={132} className={textFillStep}>
        {t("orderbook.tier3_fill")}
      </text>

      {/* Total cost formula */}
      <text
        x={300}
        y={158}
        className={light ? "fill-gray-800 font-sans text-[10.5px] font-semibold" : "fill-gray-800 dark:fill-gray-200 font-sans text-[10.5px] font-semibold"}
      >
        {t("orderbook.total_cost")}
      </text>

      {/* Result Callout Box */}
      <rect
        x={298}
        y={170}
        width={238}
        height={66}
        rx={6}
        className={calloutBg}
        strokeWidth={1}
      />
      <text x={312} y={192} className="font-sans text-[11px]">
        <tspan className={light ? "fill-gray-700 font-medium" : "fill-gray-700 dark:fill-gray-300 font-medium"}>
          {t("orderbook.visible_price")}
        </tspan>
        <tspan className={light ? "fill-gray-400" : "fill-gray-400 dark:fill-gray-500"}>
          {"  →  "}
        </tspan>
        <tspan className={light ? "fill-gray-950 font-bold" : "fill-gray-950 dark:fill-gray-100 font-bold"}>
          {t("orderbook.avg_fill")}
        </tspan>
      </text>
      <text
        x={312}
        y={218}
        className={light ? "fill-rose-700 font-mono text-[12px] font-bold" : "fill-rose-700 dark:fill-rose-400 font-mono text-[12px] font-bold"}
      >
        {t("orderbook.slippage")}
      </text>
    </svg>
  );
}
