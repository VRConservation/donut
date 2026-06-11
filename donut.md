---
title: Donut hole as landscape reslience 🔥
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
**Resilence**


# Background
> "Wildfire season is fast approaching, and with low snowpack, dry conditions, and soaring temperatures across the U.S., experts are warning that 2026 may be one of the worst on record. Combine those extreme conditions with massive restructuring at the U.S. Forest Service (USFS), and the result is a powder keg for federal wildland firefighters." @clarke

This is the 2nd of two articles examining vulnerability and resilience across California firescapes. The first [Predicting 2026 Wildfires](https://3point.xyz/predicting_fire2/) explored the potential fire vulnerability of two locations in the Sierra-Cascade region of California. This article explores more of the 'why' behind why large fires have not taken place recently in those regions and whether or not it may be due to dumb luck, or, more likely, abiotic and biotic factors.

Our main aim was to identify where intervention matters most rather than just reiterating that fire risk is high everywhere.

## Methodology
The Shasta-Trinity region did not have a mechanical treatment feasibility dataset, so we developed one using the methodology developed by @tukman. Data sources differed slightly where slope came from USGS 3DEP, and treatable vegetation from Landfire's existing vegetation type. Data was processed using a combination of python scripts and tools from QGIS and ArcGIS Pro.

# Donut holes & resilience
are these places resilient, or simply overdue?

What stands out to me is the **shift from generalized “bad fire year” narratives toward identifying concentrated areas of vulnerability** through the overlap of fire history gaps and crown-fire probability.

The “donut hole” pattern in the Sierra/Nevada region is especially useful because it raises the question of **whether some landscapes are functionally more resilient or simply overdue for a major fire**. Your point about fragmented treatment on private parcels in the WUI is important; **there is a real herd immunity metaphor in fire hardening we need to pay attention to.**  

the article is strongest when it frames the work as identifying concentrated vulnerability rather than “predicting wildfire.” 

The methodology feels more like: historical fire absence + crown-fire probability + treatment context = areas potentially vulnerable to severe fire under current conditions.

The really important systems story may actually be: climate stress + accumulated fuels + institutional weakening at the same time. That triad is what makes the current moment different.

## Avoided costs
One thing this also made me think about was the 2014 Mokelumne Watershed Avoided Cost Analysis that suggested that treatment does not necessarily need to occur everywhere equally to produce landscape-scale benefits [@moke]. It modeled that something on the order of ~30% treatment in strategically connected areas materially altered subsequent fire behavior across larger watershed systems.

What strikes me as most important there is not necessarily the exact number itself, but the larger systems implication behind it. The research seems to point toward a kind of ecological network resilience, where strategically treating enough of the right places may shift fire behavior across a broader landscape. In some ways, the herd immunity metaphor is useful here, not as a literal equivalence, but as a planning framework. If enough of a landscape is treated, connected, and stewarded appropriately, the overall probability of catastrophic crown fire may decline significantly even though not every acre is treated.

That also helps bridge the conversation toward cultural burning and long-term stewardship. Mechanical thinning is probably best understood as a transitional phase needed to bring forests back within ecological carrying capacity after a century of suppression. Over time, prescribed fire and especially cultural burning become the more durable maintenance system, restoring the patchy and heterogeneous landscapes that historically limited fire intensity and spread.

I increasingly think this same systems logic applies to communities as well. Forest tending and home hardening probably need to be understood as complementary resilience infrastructures rather than separate policy silos. A treated forest surrounding vulnerable communities behaves differently than an untreated one, just as hardened homes and defensible space function differently within landscapes burning at lower intensity. The interaction between those layers may matter as much as any single intervention.

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