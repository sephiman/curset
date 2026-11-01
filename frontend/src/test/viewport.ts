/** A `matchMedia` for jsdom that answers `max-width` queries for a fixed viewport width. */
export function setViewportWidth(width: number): void {
  window.matchMedia = (query: string): MediaQueryList => {
    const limit = /max-width:\s*([\d.]+)px/.exec(query);
    return {
      matches: limit ? width <= Number(limit[1]) : false,
      media: query,
      onchange: null,
      addEventListener: () => undefined,
      removeEventListener: () => undefined,
      addListener: () => undefined,
      removeListener: () => undefined,
      dispatchEvent: () => false,
    };
  };
}

export function clearViewport(): void {
  Reflect.deleteProperty(window, "matchMedia");
}
