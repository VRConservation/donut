---
title: Donut hole as landscape resilience 🔥
abstract: |
  "Donut hole" patterns—areas where fire has not occurred historically but are surrounded by recent large fires—in California's Sierra-Cascade region, suggest pinpointing where intervention is most necessary, rather than just stating that fire risk is high everywhere. By comparing crown fire probability with the feasibility of mechanical treatments in the four-county Central Sierra, we found only an 8% overlap. This suggests that the areas most vulnerable to fire are often on steep, remote land that is hard to access for conventional thinning. An analysis of the Interagency Tracking System data showed that treatments in Shasta and Trinity Counties do not focus as much on high-probability areas. In contrast, the Central Sierra sees 28% of treated land designated for high-risk zones. This connection acts like ecological herd immunity, reducing the severity of crown fires even without full coverage. These findings highlight a systems-based approach to resilience that combines mechanical treatment, cultural burning, home hardening, and community planning. The approach addresses the growing challenges of where to prioritize and treat landscapes to reduce fire while increasing forest health and resilience across large landscapes.

exports:
    - format: docx
      template: curvenote
      output: exports/donut.docx
    - format: pdf
      template: lapreprint-typst
      output: exports/donut.pdf  
---

# Take-aways
**1. Overlap**. The overlap between high crown fire probability and feasible mechanical treatment is low. For instance in the four county Central Sierra, these areas only overlap by 8%. While that's not great for mitigating fire, it could just mean that the most vulnerable areas aren't accessible for mechanical thinning and restoration efforts should be directed to easy to access places that prevent fire from running to higher probability areas.
<br>
**2. Resilience**. It's unclear whether or not the donut hole areas are more resilient, haven't burned due to biotic or abiotic factors, but they do point to places where a large fire may yet occur and therefore need some attention. They also offer opportunities to scale treatments due to surrounding burn lines from previous fires.
<br>
**3. Prioritization**. Using crown fire probability and recent fire history may help prioritize where future mechanical thinning and prescribed fire forest health projects could be prioritized.

# Background
> "Nevada County [is] the next [big fire]. Everybody in wildland fire knows it. The ingress, egress, how many trees are in that area. I don't want to be there...I know people are going to die in that area. Bill Jacks [@standing]

This is the 2nd of two articles examining vulnerability and resilience across California firescapes. The first [Predicting 2026 Wildfires](https://3point.xyz/predicting_fire2/) explored the potential fire vulnerability of two 'donut hole' locations in the Sierra-Cascade region of California where large, destructive fires have not occurred recently despite the existence of neighboring fires. This article explores more of the why behind why large fires have not taken place recently in those regions and whether or not it may be due to dumb luck, or, more likely, abiotic and biotic factors.

Our main aim was to identify where intervention matters most rather than just reiterating that fire risk is high everywhere after identifying historical fire absence plus crown-fire probability plus treatment context equals areas potentially vulnerable to severe fire under current conditions.

## Methodology
The Shasta-Trinity region did not have a mechanical treatment feasibility dataset, so we created one using the methodology developed by @tukman. Data sources differed slightly where slope came from USGS 3DEP, and treatable vegetation from the USGS National Land Class Dataset. Data was processed using a combination of Python, the Geospatial Data Abstraction Library (GDAL), QGIS, and ArcGIS Pro.

# Donut holes & resilience
The donut hole pattern in the Sierra/Nevada region is especially useful because it raises the question of whether some landscapes are functionally more resilient or just overdue for a major fire. These islands offer an opportunity to scale treatments to larger areas due to natural burn lines and reduced cost of constructing control lines [@wilson]. The point in the first article about the fragmented treatment of private parcels in the WUI is important; there is a real herd immunity metaphor in fire hardening that should be considered for wildfire mitigation. Shift from generalized narratives about bad fire years to identifying specific areas of vulnerability through the overlap of fire history gaps and crown-fire probability.

## Avoided costs
The 2014 Mokelumne Watershed Avoided Cost Analysis,suggested that treatment doesn’t have to occur uniformly to provide benefits across larger areas [@moke]. The study modeled that about 30% treatment in strategically connected areas can significantly change fire behavior in larger watershed systems.

What stands out is not just the specific number but the broader implications for systems. The research suggests a kind of resilience in ecological networks, where treating the right areas can influence fire behavior across wider landscapes. The metaphor of herd immunity is useful here, not as a direct comparison, but as a way to think about planning. If enough of a landscape is treated and cared for, the likelihood of severe crown fires may decrease, even if not every acre gets treated.

This perspective also connects to cultural burning and long-term stewardship. Mechanical thinning is likely best seen as a transitional step to restore forests to their natural capacity after a century of fire suppression. Over time, prescribed fire and especially cultural burning can become the lasting maintenance approach that restores the varied landscapes that historically limited fire intensity and spread.

This same systems thinking applies to communities as well. Forest care and home hardening should be seen as complementary elements of resilience, not separate policies. A treated forest around vulnerable communities reacts differently than one that is untreated, just as hardened homes and defensible space perform differently in areas experiencing lower-intensity fires. The interaction between these elements may be as important as any individual intervention.

## Biomass and fire
We calculated the percent overlap between crown fire probability [@pyrologix] and mechanical treament feasibility for the four county Central Sierra region [@scenarioA] where the treatment feasibility is <35% slopes and within 1000' (just over 300m) of existing roads {numref}`over`. We did not examine this in depth for the Shasta-Trinity region since the resulting mechanical treatment feasibility map for the region had 19% overlap for ok for treatment with high (>70%) crown fire probability. One minor difference is the mechanical treatment feasibility is <35% slopes in the Sierra but <40% for the Shasta-Trinity County region.

:::{figure} Overlap_all.png
:label: over
:height: 700
Crown fire probability vs. mechanical treatment feasibility (<35% slopes and within 1000',just over 300m, of existing roads>). The calculated overlap between the two datasets is 8% in the Sierra and 19% in the Cascades.
:::

Interestingly, only 8% of the treatment feasibility overlapped with crown fire probability in the Central Sierra region. This is likely because the most vulnerable areas, those with the highest probability of crown fire, may exist on steeper, more remote slopes making them difficult to access for mechanical treatment. Although this is alarming from a mechanical treatment perspective, it could be that these areas' lack of accessibility may make them less prone to human-induced ignitions.

## Inter-agency Tracking System
On the other hand, if we examine treatments recorded in the Interagency Tracking System treatment tracker there is overlap between treatments and areas of high probability ({numref}`treatments`). Keep in mind that the polygons are large (10,000 ac) and the probabilities represent the median for the entire polygon. As a result, even small treatments could make a big difference over those relatively large landscapes.

:::{figure} its.png
:label: treatments
:height: 700
Crown fire probability vs. Interagency Tracking System treatments. There are more treatments in the Central Sierra high probability areas vs. the donut in the Cascades. In fact, the high probability region in northeast Shasta County does not have many treatments.
:::

Examining this quantitatively, it's clear that the treatments in Shasta/Trinity Counties ({numref}`shasta`) are not as focused on high probability acres as the Sierra Counties ({numref}`sierra`). 

:::{figure} shasta_binned.png
:label: shasta
:height: 350
Crown fire probablity vs. percent area treated in Shasta and Trinity Counties. Low 60%, Medium 32%, High 8%.
:::

:::{figure} sierra_binned.png
:label: sierra
:height: 350
Crown fire probablity vs. percent area treated in Central Sierra Counties. Low 18%, Medium 54%, High 28%.
:::

## Wind speed
Anecdotally, the four county region in the Central Sierra (Nevada, Placer, Sierra, Yuba) has not had a catastrophic wildfire recently because the region has particularly low winds. We examined whether or not there were any such anomalies using a global wind dataset and did not find anything that stood out [@wind]. This could still be the case at local levels, but we have not yet found data to indicate this is the case.

# Applications
Donut hole patterns provide a practical way to pinpoint where wildfire intervention is most needed. In the Central Sierra, only 8% of high crown fire probability overlaps with areas that can be treated mechanically. The locations most at risk for severe fire are often the hardest to access. Still, strategic prioritization is essential. 

This analysis can help identify where restoration can realistically scale quickly enough to be effective. 