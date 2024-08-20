## Annotations

Halcyon uses [Open Geospatial Consortium (OSC) GeoSPARQL](http://www.geosparql.org/) for its annotations.  Given its RDF basis, it's possible to use [Turtle](https://www.w3.org/TR/turtle/), [RDF-XML](https://www.w3.org/TR/rdf-syntax-grammar/), or [JSON-LD](https://www.w3.org/TR/json-ld11/) for your format.  The latest developments for GeoSPARQL can be seen at their [GitHub repository](https://github.com/opengeospatial/ogc-geosparql).

Here is an example of GeoSPARQL in Turtle:
```
@prefix dc:   <http://purl.org/dc/terms/> .
@prefix exif: <http://www.w3.org/2003/12/exif/ns#> .
@prefix geo:  <http://www.opengis.net/ont/geosparql#> .
@prefix hal:  <https://halcyon.is/ns/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sno:  <http://snomed.info/id/> .
@prefix so:   <https://schema.org/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

<urn:md5:a923c8367e61792f531e65d966d4cb78>
        a            so:ImageObject;
        exif:height  "82984"^^xsd:int;
        exif:width   "112231"^^xsd:int .

[ a                    geo:FeatureCollection;

  dc:creator           "http://orcid.org/0000-0003-0223-1059";
  dc:date              "2023-11-09T19:48:15.406625700Z"^^xsd:dateTime;
  dc:description       "Nuclear segmentation of TCGA cancer types";
  dc:publisher         <https://ror.org/01882y777> , <https://ror.org/05qghxh33>;
  dc:references        "https://doi.org/10.1038/s41597-020-0528-1";
  dc:title             "cnn-nuclear-segmentations-2019";
  prov:wasGeneratedBy  [ a                       prov:Activity;
                         prov:used               <urn:md5:a923c8367e61792f531e65d966d4cb78>;
                         prov:wasAssociatedWith  <https://github.com/SBU-BMI/quip_cnn_segmentation/releases/tag/v1.1>
                       ];					   
					   
  rdfs:member          [ a                   geo:Feature;
                         geo:hasGeometry     [ geo:asWKT  "POLYGON ((69379 61479, 69378 61480, 69373 61480, 69370 61483, 69370 61492, 69371 61493, 69371 61494, 69372 61495, 69373 61495, 69374 61496, 69375 61496, 69376 61495, 69379 61495, 69380 61494, 69381 61494, 69383 61492, 69384 61492, 69385 61491, 69385 61490, 69386 61489, 69386 61488, 69387 61487, 69387 61483, 69384 61480, 69383 61480, 69379 61479))" ];
                         hal:classification  sno:48512009;
                         hal:measurement     [ hal:classification  sno:48512009;
                                               hal:hasProbability  "1.0"^^xsd:float
                                             ]
                       ];
  rdfs:member          [ a                   geo:Feature;
                         geo:hasGeometry     [ geo:asWKT  "POLYGON ((87135 28142, 87134 28143, 87133 28143, 87133 28144, 87132 28145, 87132 28146, 87131 28147, 87131 28160, 87132 28161, 87132 28163, 87134 28165, 87135 28165, 87137 28167, 87138 28167, 87140 28169, 87141 28169, 87142 28170, 87147 28170, 87147 28169, 87148 28168, 87148 28158, 87149 28157, 87149 28156, 87150 28155, 87151 28155, 87152 28154, 87152 28151, 87147 28146, 87146 28146, 87145 28145, 87144 28145, 87135 28142))" ];
                         hal:classification  sno:48512009;
                         hal:measurement     [ hal:classification  sno:48512009;
                                               hal:hasProbability  "1.0"^^xsd:float
                                             ]
                       ];
  rdfs:member          [ a                   geo:Feature;
                         geo:hasGeometry     [ geo:asWKT  "POLYGON ((90041 34682, 90040 34683, 90035 34683, 90031 34687, 90031 34688, 90030 34689, 90030 34690, 90031 34691, 90031 34694, 90034 34697, 90034 34698, 90036 34700, 90037 34700, 90039 34702, 90040 34702, 90041 34703, 90042 34703, 90043 34704, 90044 34704, 90045 34705, 90046 34705, 90047 34706, 90048 34706, 90049 34707, 90062 34707, 90063 34706, 90065 34706, 90066 34705, 90067 34705, 90067 34704, 90068 34703, 90068 34700, 90067 34699, 90067 34693, 90066 34692, 90065 34692, 90062 34689, 90060 34689, 90059 34688, 90057 34688, 90056 34687, 90054 34687, 90053 34686, 90052 34686, 90051 34685, 90050 34685, 90041 34682))" ];
                         hal:classification  sno:48512009;
                         hal:measurement     [ hal:classification  sno:48512009;
                                               hal:hasProbability  "1.0"^^xsd:float
                                             ]
                       ];
  rdfs:member          [ a                   geo:Feature;
                         geo:hasGeometry     [ geo:asWKT  "POLYGON ((49207 26483, 49206 26484, 49205 26484, 49202 26487, 49201 26487, 49199 26489, 49199 26490, 49198 26491, 49198 26493, 49197 26494, 49198 26495, 49198 26498, 49199 26499, 49199 26500, 49201 26502, 49202 26502, 49203 26503, 49204 26503, 49205 26504, 49211 26504, 49213 26502, 49214 26502, 49215 26501, 49215 26500, 49216 26499, 49216 26496, 49217 26495, 49217 26487, 49214 26484, 49213 26484, 49207 26483))" ];
                         hal:classification  sno:48512009;
                         hal:measurement     [ hal:classification  sno:48512009;
                                               hal:hasProbability  "1.0"^^xsd:float
                                             ]
                       ]
] .
```
Let's break this down a bit.  First is the top defintion of the GeoSparql Feature Collection.
```
[ a                    geo:FeatureCollection;

  dc:creator           "http://orcid.org/0000-0003-0223-1059";
  dc:date              "2023-11-09T19:48:15.406625700Z"^^xsd:dateTime;
  dc:description       "Nuclear segmentation of TCGA cancer types";
  dc:publisher         <https://ror.org/01882y777> , <https://ror.org/05qghxh33>;
  dc:references        "https://doi.org/10.1038/s41597-020-0528-1";
  dc:title             "cnn-nuclear-segmentations-2019";
  prov:wasGeneratedBy  [ a                       prov:Activity;
                         prov:used               <urn:md5:a923c8367e61792f531e65d966d4cb78>;
                         prov:wasAssociatedWith  <https://github.com/SBU-BMI/quip_cnn_segmentation/releases/tag/v1.1>
                       ]; 
```
The feature collection basic metadata is in [Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) and the [PROV Ontology](https://www.w3.org/TR/prov-o/).  The piece critical for this GeoSPARQL file to work with Halcyon is the prov:wasGeneratedBy which defines the process by which the data was created and the source image to which that process acted upon.  Halcyon uses the MD5 hash of the image to make it easy for the system to link images to associated Feature Collections.

Expressed as JSON-LD
```
{
    "@context": "https://halcyon.is/context.json",
    "@type": "FeatureCollection",
    "dc:creator": "http://orcid.org/0000-0003-0223-1059",
    "date": "2023-11-09T19:48:15.406625700Z",
    "description": "Nuclear segmentation of TCGA cancer types",
    "publisher": [
        "https://ror.org/05qghxh33",
        "https://ror.org/01882y777"
    ],
    "dc:references": "https://doi.org/10.1038/s41597-020-0528-1",
    "title": "cnn-nuclear-segmentations-2019",
    "wasGeneratedBy": {
        "@type": "Activity",
        "used": {
            "@id": "urn:md5:a923c8367e61792f531e65d966d4cb78",
            "@type": "ImageObject",
            "height": 82984,
            "width": 112231
        },
        "wasAssociatedWith": "https://github.com/SBU-BMI/quip_cnn_segmentation/releases/tag/v1.1"
    },
    "member": [
        {
            "@type": "Feature",
            "geometry": {
                "asWKT": "POLYGON ((49207 26483, 49206 26484, 49205 26484, 49202 26487, 49201 26487, 49199 26489, 49199 26490, 49198 26491, 49198 26493, 49197 26494, 49198 26495, 49198 26498, 49199 26499, 49199 26500, 49201 26502, 49202 26502, 49203 26503, 49204 26503, 49205 26504, 49211 26504, 49213 26502, 49214 26502, 49215 26501, 49215 26500, 49216 26499, 49216 26496, 49217 26495, 49217 26487, 49214 26484, 49213 26484, 49207 26483))"
            },
            "classification": "sno:48512009",
            "measurement": {
                "classification": "sno:48512009",
                "hasProbability": 1.0
            }
        },
        {
            "@type": "Feature",
            "geometry": {
                "asWKT": "POLYGON ((90041 34682, 90040 34683, 90035 34683, 90031 34687, 90031 34688, 90030 34689, 90030 34690, 90031 34691, 90031 34694, 90034 34697, 90034 34698, 90036 34700, 90037 34700, 90039 34702, 90040 34702, 90041 34703, 90042 34703, 90043 34704, 90044 34704, 90045 34705, 90046 34705, 90047 34706, 90048 34706, 90049 34707, 90062 34707, 90063 34706, 90065 34706, 90066 34705, 90067 34705, 90067 34704, 90068 34703, 90068 34700, 90067 34699, 90067 34693, 90066 34692, 90065 34692, 90062 34689, 90060 34689, 90059 34688, 90057 34688, 90056 34687, 90054 34687, 90053 34686, 90052 34686, 90051 34685, 90050 34685, 90041 34682))"
            },
            "classification": "sno:48512009",
            "measurement": {
                "classification": "sno:48512009",
                "hasProbability": 1.0
            }
        },
        {
            "@type": "Feature",
            "geometry": {
                "asWKT": "POLYGON ((87135 28142, 87134 28143, 87133 28143, 87133 28144, 87132 28145, 87132 28146, 87131 28147, 87131 28160, 87132 28161, 87132 28163, 87134 28165, 87135 28165, 87137 28167, 87138 28167, 87140 28169, 87141 28169, 87142 28170, 87147 28170, 87147 28169, 87148 28168, 87148 28158, 87149 28157, 87149 28156, 87150 28155, 87151 28155, 87152 28154, 87152 28151, 87147 28146, 87146 28146, 87145 28145, 87144 28145, 87135 28142))"
            },
            "classification": "sno:48512009",
            "measurement": {
                "classification": "sno:48512009",
                "hasProbability": 1.0
            }
        },
        {
            "@type": "Feature",
            "geometry": {
                "asWKT": "POLYGON ((69379 61479, 69378 61480, 69373 61480, 69370 61483, 69370 61492, 69371 61493, 69371 61494, 69372 61495, 69373 61495, 69374 61496, 69375 61496, 69376 61495, 69379 61495, 69380 61494, 69381 61494, 69383 61492, 69384 61492, 69385 61491, 69385 61490, 69386 61489, 69386 61488, 69387 61487, 69387 61483, 69384 61480, 69383 61480, 69379 61479))"
            },
            "classification": "sno:48512009",
            "measurement": {
                "classification": "sno:48512009",
                "hasProbability": 1.0
            }
        }
    ]
}
```
