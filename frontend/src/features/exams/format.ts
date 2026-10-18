/** «Simulacro» or «Tema · El recurso de alzada»: the preset, and what a parametric one was sat on. */
export function sittingName(sitting: { presetTitle: string; targetTitle: string | null }): string {
  return sitting.targetTitle ? `${sitting.presetTitle} · ${sitting.targetTitle}` : sitting.presetTitle;
}

/** Two decimals with the reader's separator: a transformed score is not a percentage. */
export function scoreNumber(value: number, locale: string | undefined): string {
  return value.toLocaleString(locale, { minimumFractionDigits: 0, maximumFractionDigits: 2 });
}

/** A sitting's headline: the transformed total out of its maximum when the preset scores, else the share right. */
export function examScore(
  result: { score: number | null; transformed?: number | null; max?: number | null },
  locale?: string,
): string {
  if (result.transformed != null && result.max != null) {
    return `${scoreNumber(result.transformed, locale)} / ${scoreNumber(result.max, locale)}`;
  }
  if (result.score == null) return "—";
  return `${Math.round(result.score * 100)}%`;
}

/** «1 h 23 min» / «12:05»: what is left on the clock, from milliseconds. */
export function clock(ms: number): string {
  const total = Math.max(0, Math.floor(ms / 1000));
  const hours = Math.floor(total / 3600);
  const minutes = Math.floor((total % 3600) / 60);
  const seconds = total % 60;
  const pad = (n: number) => String(n).padStart(2, "0");
  return hours > 0 ? `${hours}:${pad(minutes)}:${pad(seconds)}` : `${pad(minutes)}:${pad(seconds)}`;
}
