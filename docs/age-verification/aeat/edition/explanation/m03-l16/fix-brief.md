# Fix brief — `m03-l16`

## caso:### Deducción por maternidad#1

Current: Sara está dada de alta en la Seguridad Social y tiene una hija nacida el lunes 12 de enero de 2026, con derecho al mínimo por descendientes. Puede minorar la cuota diferencial hasta en 1.200 euros anuales mientras la hija no cumpla tres años (art. 81.1 LIRPF). Si paga en 2026 una guardería autorizada, 1.800 euros, la deducción se puede incrementar hasta en 1.000 euros adicionales, hasta 2.200 euros (art. 81.2 LIRPF).

Blind verifier: FAIL — «Sara está dada de alta en la Seguridad Social ... Puede minorar la cuota diferencial hasta en 1.200 euros» omite una condición del 81.1: el alta exige «un período mínimo ... de 30 días cotizados». Sin ella no hay derecho a la deducción ni al incremento por guardería. El resto (1.000 adicionales con 1.800 de gasto, hasta 2.200; lunes 12-1-2026) es correcto.
Student reader: REWRITE — It says "hasta 2.200" with 1.800 paid in nursery fees without saying the increase is capped at 1.000, so a reader may add the 1.800; the birth weekday is noise.

