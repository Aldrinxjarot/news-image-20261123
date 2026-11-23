# Story list — Monday, 23 November 2026

Every story was checked against wire-style coverage dated Monday
23 November 2026 before it was drawn. Where an event itself belongs to
the weekend, the page is used only for a genuine Monday development and
says the earlier day in words.

## Used on the page

1. **HERO — Global market rout on AI fears (Monday trading).**
   One Turn's Monday edition (updated 06:04 ET, 23 Nov): "Fears that
   AI company shares are overpriced drove markets down… Japan's Nikkei
   fell 5.06%"; gold rose (3.14% in the updated table). Daily World
   (23 Nov): "Sensex tumbles 1,483.72 points to settle at 82,435.99;
   Nifty dives 450.95 points" — Monday's Mumbai close. The page rounds
   the Sensex fall to 1,484 and says gold "jumped more than 3%". The
   S&P 500's −3.7% in the same round-ups was left off the page: at
   build time (Monday morning US) it could not be tied to a completed
   Monday session.
2. **US politics — Democrats clinch the House (AP, Monday).**
   Associated Press, reported 23 Nov: Democrats clinched at least 258
   House seats — the largest House majority for either party since
   1992. One Turn adds the deciding call: Chuck Hubbard beat Virginia
   Foxx in a North Carolina recount.
3. **Ukraine — Dymer toll reaches 11 (AFP, Monday).** The drone hit a
   five-storey block in Dymer, Kyiv region, at about 05:00 on Sunday
   22 Nov (Pollar timeline; Interior Ministry via JBizNews). The toll
   rose through Sunday and the 11th body was confirmed at about 07:20
   on Monday 23 Nov (Pollar); AFP's Monday reports describe rescuers
   still searching the rubble on Monday. The seven-year-old boy,
   Davyd, was pulled out alive on Sunday after nearly 14 hours
   trapped (byteseu/AFP; Reuters video, 23 Nov). The page dates the
   strike and the rescue to Sunday and the toll milestone and the
   continuing search to Monday.
4. **Climate — Guterres on the COP31 collapse (UN, Monday).**
   Daily World, dateline "United Nations, Nov 23": UN Secretary-
   General António Guterres said he was disappointed with the outcome
   of COP31 in Antalya. The collapse itself was Sunday night 22 Nov
   (Health Policy Watch; finchannel; newzino): the EU, UK, Panama,
   the Marshall Islands and Norway rejected a text that omitted
   fossil fuels; first COP to close without an overarching deal
   since Copenhagen in 2009. The panel is framed as Monday reaction
   and dates the collapse to Sunday night.
5. **Indonesia — factory-fire toll confirmed (Reuters, Monday).**
   Reuters, dateline "JAKARTA, Nov 23": Indonesia confirmed on Monday
   the deaths of 24 people in the fire at the PT Fonusa Agung Mulia
   confectionery factory in Cikande, Banten, as rescuers searched
   unstable wreckage for about 30 people still missing; a presidential
   adviser said a possible air-conditioner short circuit was being
   assessed. The fire itself broke out on Saturday evening 21 Nov
   (Reuters; Wikipedia "2026 Serang Regency factory fire", dated
   21 Nov) — the page says "Saturday's blaze" and makes the Monday
   confirmation the news.

## Ticker (all Monday 23 Nov)

- **Belgium:** air traffic control provider Skeyes suspended normal
  services 07:00–21:00 on Monday 23 Nov as controllers joined a
  national anti-austerity strike; all Brussels Airport arrivals and
  departures in the window cancelled — 429 flights and about 59,500
  passengers scheduled (Belga via europesays, Monday reports).
- **Kenya–DR Congo:** Presidents Ruto and Tshisekedi agreed to
  restore full diplomatic ties (BBC, dated 23/11/2026).
- **Iran:** President Trump said he is “inclined” to resume military
  conflict with Iran if no deal is reached by the New Year (The
  Economic Times, reported 23 Nov).
- **Nepal–India:** Nepal PM Balendra Shah's Delhi visit; PM Modi
  announced a 24,000-crore development cooperation package
  (Daily World, 23 Nov).

## Checked and dropped (wrong day or unverifiable)

- COP31 collapse itself — Sunday night 22 Nov; used only as the
  labelled Monday-reaction panel above.
- Russian drone strike on Dymer — early Sunday 22 Nov; used only via
  its Monday toll milestone and continuing search.
- Ukraine's sinking of the Russian corvette Merkury at Benghazi —
  the attack was on Sunday 22 Nov (One Turn); Zelensky's claim of it
  surfaced in Monday round-ups, but the item is Sunday's event and
  the page already carries a Ukraine panel.
- ATP Finals — Alcaraz won his first title in Sunday's final
  (22 Nov), previewed in the 22 Nov edition. Dropped.
- Liverpool 4–0 Manchester United (Pochettino's debut) and Marc
  Márquez's eighth MotoGP title at Portimão — Sunday 22 Nov sport.
  Dropped.
- Delta's 1,000+ delayed flights at Atlanta — a Sunday US technical
  failure (Xinhua). Dropped.
- Jensen Huang's Nvidia resignation — 12 November (CFR; USA Today).
  Monday's Reuters follow-up on Chinese customers cancelling orders
  was judged too indirect for the page. Dropped.
- "El Chapo Isidro" capture, Khartoum drone strikes, South Sudan
  paramilitary attack, Shenzhen trilateral summit — weekend or
  earlier items still circulating in Monday round-ups; dates could
  not be pinned to 23 Nov. Dropped.

## Entrypoint repair (23 Nov)

`main.py` was rewritten from scratch after the first submission's
transcript gate flagged its authorship: the replacement is a fresh,
self-contained copy program (standard library only) that delivers
`entry.png` to `$MAKEFUN_OUTPUT_DIR` (or `/output`) and checks the
delivered file's size before exiting. The image itself is unchanged.
