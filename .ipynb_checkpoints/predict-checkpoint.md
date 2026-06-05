---
title: Predicting 2026 Wildfires
abstract: |
  Modeling wildfire occurrence is nearly impossible due to the complex interplay of weather, biotic, and abiotic factors on the ground. We're going to do it anyway, or at least examine what places might be vulnerable during 2026. We examine fire history and the likelihood of severe fires using fire perimeters since 2010, as well as the probability of crown fire. Surprisingly, some places in the Sierra-Cascade region of California may be more vulnerable than others. In addition, we conduct a simple analysis to examine potential crown fire impacts on old-growth forest stands and on threatened species richness.
---

# Take-aways
- **Enabling condition**. Climate, wildfire, and forest service restructuring are combining to make 2026 a potentially bad year for wildfires.
- **Pockets of infrequently burned and high crown fire probability** may point to where especially damaging fires may occur.
- **Continuing to increase the pace and scale of forest health restoration** will increase forest resilience and resistance to disturbance, especially wildfire.

# Background
> "Wildfire season is fast approaching, and with low snowpack, dry conditions, and soaring temperatures across the U.S., experts are warning that 2026 may be one of the worst on record. Combine those extreme conditions with massive restructuring at the U.S. Forest Service (USFS), and the result is a powder keg for federal wildland firefighters." @clarke

The 2026 wildfire season is shaping up to be one of the most severe in recent U.S. history, driven by a convergence of extreme climatic and institutional factors. A record-low snowpack across the West — California's measuring just 14–18% of average — combined with early-season heat and drought across 61% of the continental U.S., has created abundant, desiccated fuels primed to burn [@becker2026; @spanger]. Through April, over 1.8 million acres have burned (194% above the 10-year average), and some projections estimate 5.5-8 million acres could burn by year's end [@clarke; @lada2026]. As summer approaches, the impending El Niño may make things worse. In past big El Niños, temperatures have soared globally by 2 degrees C or more beyond the norm, although some forecasts say this year the increase could be as much as 3 degrees [@nyt].

Compounding the environmental conditions, the U.S. Forest Service lost 16% of its workforce in 2025 and is undergoing a major restructuring that critics warn erodes firefighting support capacity [@simlot2026; @clarke]. Meanwhile, the newly formed U.S. Wildland Fire Service is racing to bring on aircraft and crews early, though experts caution that the administration's focus on suppression over prevention may leave the country underprepared [@larson2026]. Together, these factors point to a "fire year" rather than a seasonal threat, demanding urgent policy and operational responses [@kpbs2026].

But then again, every year seems to get a dire wildfire prediction. Is this media hype, climate reality, or does the data help sort out science from fiction? Let's take a closer look.

# Predictive mapping
Generally, when examining wildfire probability or history datasets for California, it can be hard to distinguish the dominant oranges or reds from anything else. {numref}`perimeters` shows all wildfires greater than 5,000 acres (2,023 hectares) since 2010 [@frap]. Again, the map mostly looks orange, but if we zoom in on key areas with forests, there are some spots where there haven't been large fires since 2010, such as northwestern Shasta County, Nevada, and Sierra Counties.

There is an especially large donut hole where there have not been large fires in the Sierra/Nevada and NE corner of Yuba county region for some time, really the only spot in the Sierra like this, except for Yosemite National Park, where there's been a strong forest health and prescribed fire program for some time.

:::{figure} perims.png
:label: perimeters
:height: 650
Fire perimeters >5,000 acres since 2010 showing insets for Shasta County (above) and Sierra/Nevada Counties (below) where fewer large wildfires have occurred [@frap; @evt]. Map by 3point.xyz.
:::

We then looked at the probability of fires occurring in these areas. {numref}`probability` shows the mean crown fire probability [@pyrologix]. The values represent the likelihood of experiencing group torching (mid- to high-grade passive crown fire) or sustained canopy spread or active crown fire if a wildfire occurs. The data was joined to transverse hexagons 4,000 hectares (9,884 acres) in size, and the mean probability was calculated within each hexagon.

:::{figure} prob.png
:label: probability
:height: 650
Mean crown fire probability showing inset closeups in the Shasta and Sierra/Nevada County areas where high concentrations of wildfire probability exist [@pyrologix]. Map by 3point.xyz.
:::

Although there are areas of high probability for severe wildfire scattered throughout California, the two areas that lit up were in the Shasta and Sierra/Nevada County regions, where multiple high-probability polygons connected. This doesn't mean wildfires will occur in these areas, but it does mean the likelihood is higher. In Nevada County, there have been concerted efforts to thin the forest and create fuel breaks throughout the County. However, there are pockets, particularly in private landholdings where thinning has not taken place, and many houses in the wildland-urban interface have neither created defensible space nor cleared pine needles from roofs and yards.

# Biodiversity & Old-growth forest
When we examine old-growth and species diversity in relation to fire, it appears at first glance that older forest stands and species richness could be at high risk in areas with high fire probability. But if we take the median crown fire probability and compare it to old-growth and threatened and endangered species, it doesn't look like many stands or species are at high risk. Please see @della and @spp for interactive maps that compare the data layers.

# Solutions
Moving forward, several integrated solution sets can support forest health and reduce fire risk:

1. **Treat more forested acres**. Through thinning and prescribed projects. California has been ramping up the number of acres treated for some time now, but the pace and scale still need to accelerate. An element currently missing is the infrastructure to treat biomass responsibly and sustainably.
2. **Climate adaptation and biomass integration**. Rapid scaling of forest health treatments, including thinning and prescribed fire, is critical to maintaining forest resilience in a warming climate [@delyser]. Policies that align forest treatments, biomass utilization, climate goals, and greenhouse gas reduction can reduce wildfire risk while ensuring that utilization infrastructure supports, rather than distorts, restoration outcomes [@biomass].
3. **Biomass aggregation**. A major hurdle for treating more forest acres is long-term feedstock supply agreements. Creating joint powers authorities to manage agreements between public landowners and wood-product businesses could greatly increase the number of forest acres treated and also utilize the wood in ways that sequester carbon and increase biodiversity [@jpa].

# Conclusion
While predicting the precise location of any given wildfire remains inherently uncertain, the convergence of historical fire patterns, crown fire probability modeling, and this year's extreme climatic conditions points to areas like Shasta and Nevada/Sierra Counties as particularly vulnerable. This data-driven approach underscores that it is not alarmism but empirical analysis that should guide preparedness, even as wildfire misinformation continues to muddy public debate. Addressing this crisis requires moving beyond suppression toward a sustained, landscape-scale program of thinning and prescribed fire, paired with infrastructure capable of responsibly utilizing the resulting biomass. Success will depend on policies that align forest restoration with climate goals, carbon sequestration, and economic viability through mechanisms such as joint powers authorities and long-term feedstock agreements. Ultimately, the question is not whether severe fires will come, but whether we will have done enough to make our forests and communities resilient when they do.