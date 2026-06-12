---
title: Donut hole as landscape resilience 🔥
abstract: |
  Using lack of fire to interrogate landscape resilience and identifying where intervention matters most rather than just reiterating that fire risk is high everywhere.

exports:
    - format: docx
      template: curvenote
      output: exports/donut.docx
    - format: pdf
      template: lapreprint-typst
      output: exports/donut.pdf  
---

# Take-aways
**Overlap**. 
**Resilience**


# Background
> "Wildfire season is fast approaching, and with low snowpack, dry conditions, and soaring temperatures across the U.S., experts are warning that 2026 may be one of the worst on record. Combine those extreme conditions with massive restructuring at the U.S. Forest Service (USFS), and the result is a powder keg for federal wildland firefighters." @clarke

This is the 2nd of two articles examining vulnerability and resilience across California firescapes. The first [Predicting 2026 Wildfires](https://3point.xyz/predicting_fire2/) explored the potential fire vulnerability of two locations in the Sierra-Cascade region of California. This article explores more of the 'why' behind why large fires have not taken place recently in those regions and whether or not it may be due to dumb luck, or, more likely, abiotic and biotic factors.

Our main aim was to identify where intervention matters most rather than just reiterating that fire risk is high everywhere.

## Methodology
The Shasta-Trinity region did not have a mechanical treatment feasibility dataset, so we developed one using the methodology developed by @tukman. Data sources differed slightly where slope came from USGS 3DEP, and treatable vegetation from Landfire's existing vegetation type. Data was processed using a combination of python scripts and tools from QGIS and ArcGIS Pro.


The methodology feels more like this: historical fire absence plus crown-fire probability plus treatment context equals areas potentially vulnerable to severe fire under current conditions.


# Donut holes & resilience
The “donut hole” pattern in the Sierra/Nevada region is especially useful because it raises the question of whether some landscapes are functionally more resilient or just overdue for a major fire. Your point about the fragmented treatment of private parcels in the WUI is important; there is a real herd immunity metaphor in fire hardening that we need to consider. Shift from generalized narratives about “bad fire years” to identifying specific areas of vulnerability through the overlap of fire history gaps and crown-fire probability.

## Avoided costs
The 2014 Mokelumne Watershed Avoided Cost Analysis,suggested that treatment doesn’t have to occur uniformly to provide benefits across larger areas [@moke]. The study modeled that about 30% treatment in strategically connected areas can significantly change fire behavior in larger watershed systems.

What stands out is not just the specific number but the broader implications for systems. The research suggests a kind of resilience in ecological networks, where treating the right areas can influence fire behavior across wider landscapes. The metaphor of herd immunity is useful here, not as a direct comparison, but as a way to think about planning. If enough of a landscape is treated and cared for, the likelihood of severe crown fires may decrease, even if not every acre gets treated.

This perspective also connects to cultural burning and long-term stewardship. Mechanical thinning is likely best seen as a transitional step to restore forests to their natural capacity after a century of fire suppression. Over time, prescribed fire and especially cultural burning can become the lasting maintenance approach that restores the varied landscapes that historically limited fire intensity and spread.

This same systems thinking applies to communities as well. Forest care and home hardening should be seen as complementary elements of resilience, not separate policies. A treated forest around vulnerable communities reacts differently than one that is untreated, just as hardened homes and defensible space perform differently in areas experiencing lower-intensity fires. The interaction between these elements may be as important as any individual intervention.

## Biomass and wood pathways
We calculated the percent overlap between crown fire probability [@pyrologix] and mechanical treament feasibility for the four county Central Sierra region [@scenarioA] where the treatment feasibility is <35% slopes and within 1000' (~300m) of existing roads {numref}`over`. We did not examine this for the Shasta-Trinity county region since a treatment feasibility data layer does not yet exist.

:::{figure} overlap.png
:label: over
:height: 700
Crown fire probability vs. mechanical treatment feasibility (<35% slopes and within 1000',~300m, of existing roads>). The calculated overlap between the two datasets is 8%.
:::

Interestingly, most of the treatment feasibility did not overlap with crown fire probability—only 8%—possibly because areas of higher probability may exist on steeper, more remote slopes. Although this is alarming from a wildfire mitigation treatment perspective, e.g., inability to treat the most vulnerable areas, it could be that these areas lack of accessibility may make them less prone to human induced ignitions.

## Wind speed
Anecdotally, the four county region in the Central Sierra (Nevada, Placer, Sierra, Yuba) has not had a catastrophic wildfire recently because the region has particularly low winds. We examined whether or not there were any such anomalies using a global wind dataset and did not find anything that stood out [@wind]. This could still be the case at local levels, but we have not yet found data to indicate this is the case.

# Conclusions & next steps
One potentially useful next step might be looking at overlap between crown-fire probability, ownership patterns, and feasible treatment/utilization infrastructure, essentially where restoration could realistically scale fast enough to matter.

The really important systems story may actually be climate stress combined with accumulated fuels and institutional weakening at the same time. That triad is what makes this moment different.