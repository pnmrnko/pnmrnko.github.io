---
title: "Elliptical toponyms, or why we must pay attention to generic terms in names"
slug: elliptical-toponyms
date: 2026-02-08T15:00:00+03:00
toc: true
---

The seriousness with which the OpenStreetMap community approaches discussions is a true strength of the project. Over years of debate, the community has formed a highly cohesive [tagging system for names](https://wiki.openstreetmap.org/wiki/Names). These guidelines are simple for beginners, yet they allow for the precise classification and mapping of real-world names. A name is perhaps the most vital piece of data for most users—it is what they want to see on screens and paper, hear via voice navigation, and even [touch](https://en.wikipedia.org/wiki/Tactile_graphic).

However, this post isn't about which tag to choose, but rather the format in which the name should be entered. I want to discuss the phenomenon of **ellipsis**—or, to put it simply, the shortening of names—and what we as mappers should watch out for when collecting and adding toponyms to the map.

## What are elliptical toponyms?

Elliptical toponyms are geographical proper names that have been historically truncated or shortened in oral or written use. These are often names that originally included a **generic term** (a word indicating the type of object), which over time partially or completely disappeared. The table below shows several examples of such "shortened" Scandinavian and Baltic toponyms:

| Historical Full Form | Truncated Form | Explanation |
| --- | --- | --- |
| Sed-ezeris | Sedzeris | The hydronym "Lake Seda" lost the generic term *ezeris* (lake). |
| Spanggroben | Spanget | A neighborhood near a stream; the second element *-groben* (ditch/trench) was dropped. |
| Stampedam | Stampen | A farmstead near a pond; the second element *-dam* (pond) was dropped, leaving only the specific element. |
| Sankt Peters Kirche | Sankt Peter | St. Peter's Church; the second element *Kirche* (church) was dropped. |

In 1980, the Soviet linguist and translator Adolf Turkin wrote an article titled "[Elliptical Names in Komi Toponymy](https://www.researchgate.net/publication/378539756_ELLIPTIROVANNYE_NAZVANIA_V_KOMI_TOPONIMII)" about this phenomenon, providing many examples of name evolution where the suffix indicating the object type was eventually discarded. You can see a few of these in the table below:

| Historical Full Form | Truncated Form | Translation & Generic Term |
| --- | --- | --- |
| Kӧdzvidz | Kӧdz | "Pebble Meadow"; meadow (*-vidz*) |
| Shudayu | Shuda | "Happy River"; river (*-yu*) |
| Ozyu | Oz | "Strawberry River"; river (*-yu*) |
| Tarkamayag | Tarkama | "Pine forest full of grouse leks"; forest (*-yag*) |
| Ruchguamu | Ruchgua | "Field riddled with fox holes"; field (*-mu*) |

While these are mostly names that changed long ago, there are more modern examples. In a discussion within the OpenStreetMap Bulgaria community, I [asked a question](https://community.openstreetmap.org/t/abbreviations-in-bulgarian-street-names/136187/12) about why the generic term is omitted in all street names. It turns out that dropping the word "ulitsa" (street) is entirely natural in the Bulgarian language, and this was reflected in their local mapping practices:

| Full Name (Transliterated) | Entered in `name` tag | Context/Notes |
| --- | --- | --- |
| ulitsa "Zapadna" | Zapadna | "Zapadna" means "Western." A common directional street name. |
| ulitsa "Vladaiska" | Vladaiska | Named after the Vladaiska River, which flows through the heart of Sofia. |
| ulitsa "Uiliam Gladston" | Uiliam Gladston | Named after William Gladstone, the British statesman |

The examples above illustrate this aspect of toponymic evolution worldwide, and the latter shows that the OpenStreetMap community is an active participant in this process. While I won't presume to advise on mapping approaches in other countries, I believe I have insights to share with project contributors in Ukraine.

## Elliptical toponyms in Ukraine

What should we be paying attention to? Language is a living organism, not frozen in time, so names will naturally change. We should accept that the older a name is, the more likely it is to have undergone changes; we should record it as it exists today, not as it once was.

However, we shouldn't rush to conclude that a name is truly "elliptical." The absence of a generic word doesn't always mean the name was historically shortened. Often, it's just a convenient spoken shorthand or a result of copying from a table or list where the generic term was kept in a separate column or header. A truncated name might be copied from another map where the authors made a "creative" design choice. Ultimately, a mapper might feel the object type is "obvious anyway" and decide to make the name shorter.

Our task is **not to codify accidental simplifications**, but to verify if the short form actually lives as an independent name: is it written this way on signs, in documents, or official sources? Do people use it this way outside of a specific context? If not, the generic term is part of the name and must not be lost.

Here are examples from Serhiy Pavlenko’s 2013 book, [Microtoponyms of Chernihiv-Sivershchyna](https://chtyvo.org.ua/authors/Pavlenko_Serhii/Mikrotoponimy_Chernihovo-Siverschyny/). Reading it, one might mistakenly think these microtoponyms lack generic terms. In reality, the author lists the generic term followed by a dash and then a comma-separated list of names, omitting the term from each individual entry to save space. Many of these must be mapped in their full form:

| Name from the List | Full Name | Context/Notes |
| --- | --- | --- |
| Marusenkiv | Marusenkiv stavok | Marusenko's pond; named after a family or located near the estate of a man named Marusenko. |
| Khvynenkove | Khvynenkove boloto | Khvynenko's marsh; named after the Khvynenko family or a person with that surname. |
| Horile | Horile ozero | Burnt Lake; "Horile" literally means "burnt" or "scorched." |
| Nimetskyi | Nimetskyi kutok | German neighborhood; "kutok" (literally "corner") refers to a specific section or historical area of a settlement. |
| Kondrativ | Kondrativ kutok | Kondrat's neighborhood; named after the estate or family of a man named Kondrat. |
| Baidyne | Baidyne urochyshche | Baida tract; named after a man with the surname Baida. |
| Ostatna | Ostatna dolyna | The Last/Remaining Valley; "Ostatna" is a dialectal word for "last." Note: "dolyna" here refers to a small valley or dell. |
| Semeshkova | Semeshkova krynytsia | Semeshko's well; named after a man named Semeshko. |
| Vysoke | Vysoke urochyshche | High tract; "Vysoke" literally means "high," likely referring to its elevation. |
| Kovalivske | Kovalivske urochyshche | Koval tract; named after a man with the surname Koval (which means "Blacksmith"). |

To understand when a generic word is mandatory and when it can disappear without losing meaning, we need to look at the structure of the names themselves. Toponyms have different grammatical structures that often signal whether the generic term is an inseparable part of the proper name or merely a clarification.

## Grammatical structure of Ukrainian toponyms

### Agreed attributes (adjectives)

A large portion of proper names on the map of Ukraine are phrases with an **agreed attribute**. Usually, this is an adjective or numeral that agrees with the generic noun in gender, number, and case.

I suggest recording these in **direct syntactic order**, as prescribed by Ukrainian grammar. The agreed attribute should come first, followed by the generic noun in lowercase:

> 1-sha Sadova vulytsia, Soborna ploshcha, Turiiske ozero, Taraneva bukhta, Darnytskyi raion, Zghurivska selyshchna hromada, Krabova bukhta, Chornobylskyi kutok, Dehtiarna zatoka, Borychiv uzviz.

The generic term in such names cannot be omitted; the name would feel incomplete, even if the object type is already defined by top-level tags.

### Non-agreed attributes (genitives)

Another large share of names consists of phrases with a **non-agreed attribute**. This component is a noun in the genitive case that does not change when the generic noun's case changes. In these names, the generic term should be written first:

> ostriv Fainberha (Feinberg Island), pereval Legioniv (Legions Pass), vulytsia Kameniariv (Stonemasons Street), park Zakhysnykiv Ukrainy (Defenders of Ukraine Park), bulvar Verkhovnoi Rady (Verkhovna Rada Boulevard).

If a name looks incomplete or functions like a modifier, check your sources and use the full form including the generic word. Do not drop it, even if the object type is already specified in the tags.

### Apposition

Another type of attribute is **apposition**. Here, the generic term also comes first, followed by a noun in the nominative case that specifically identifies the object. While the previous two types require the generic term as an inseparable part, in this case, it can often be omitted if necessary. Some of the names below are traditionally used without the generic word, or the word is redundant because the mapped object already has a tag describing its type:

> ~~misto~~ Lviv (~~City of~~ Lviv), ~~selyshche~~ Losynivka (~~Settlement of~~ Losynivka), ~~selo~~ Trypillia (~~Village of~~ Trypillia), ~~richka~~ Desna (Desna ~~River~~), ~~hora~~ Hoverla (~~Mount~~ Hoverla), ~~stantsiia~~ Zhmerynka (Zhmerynka ~~Station~~), ~~avtozapravka~~ OKKO (OKKO ~~gas station~~), ~~kafe~~ Teplo (Teplo ~~Cafe~~), ~~restoran~~ McDonald’s.

However, for names of streets, lanes, and similar objects, **generic words should always be preserved**. There are no separate tags for different types of streets, and since these objects are used in addressing, their full name carries specific importance:

> vulytsia Yaremkivtsi, ploshcha Rynok, maidan Rynok, vulytsia Polivka, provulok Polivka, provulok Khutorok, provulok Romanchukiv Khutir.

## Why does this matter to us?

At first glance, debates over "tracts" (*urochyshche*) or "corners" (*kutok*) might seem like excessive academicism. However, for OpenStreetMap, the devil is in these details. Ukraine’s rich microtoponymy—all these local corners, ponds, fields, and islets—is living history. By preserving full names, we protect our regional and linguistic identity. OSM remains perhaps the only living project where we can record the names of the smallest features exactly as they have been used for generations.

*Originally posted in the [OpenStreetMap diary](https://www.openstreetmap.org/user/darkonus/diary/408211).*
