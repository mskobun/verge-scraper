## Wired

<https://www.wired.com/search/?q=&sort=publishdate+desc> only goes until page 416, 417 returns a 400. The earliest article on page 416 is published on 5th June 2022, which contradicts project requirements. There is a json API (just add format=json to query parameters), which says the total page count is 1250, and total result count is 10000, however it also does not let you go past page 416.

Example response:
<details>
```json
{
  "journey": {
    "url": "https://www.wired.com/journey/compiler/build-8f0d05bd023814a3e88fb20b05fe43c4.js"
  },
  "ads.page": {
    "channel": "misc",
    "content": {},
    "contentType": "search",
    "experiments": {},
    "keywords": {
      "copilotid": [
        ""
      ],
      "platform": [
        "verso"
      ],
      "tags": []
    },
    "server": "production",
    "slug": "search",
    "subChannel": "",
    "templateType": "mt_search"
  },
  "isNoAds": false,
  "ads.sandbox": "",
  "content4d": {
    "wordcount": 108,
    "brand": "wired",
    "topics": [
      {
        "name": "ALLBRANDS_64",
        "score": 0.5241427731910435
      },
      {
        "name": "ALLBRANDS_57",
        "score": 0.5241427731910435
      },
      {
        "name": "ALLBRANDS_28",
        "score": 0.5241427731910435
      },
      {
        "name": "ALLBRANDS_244",
        "score": 0.5241427731910435
      },
      {
        "name": "ALLBRANDS_21",
        "score": 0.5241427731910435
      },
      {
        "name": "ALLBRANDS_192",
        "score": 0.5241427731910435
      },
      {
        "name": "ALLBRANDS_56",
        "score": 0.16404386908214363
      },
      {
        "name": "ALLBRANDS_278",
        "score": 0.16404386908214363
      },
      {
        "name": "ALLBRANDS_219",
        "score": 0.13061446355268064
      },
      {
        "name": "ALLBRANDS_187",
        "score": 0.13061446355268064
      },
      {
        "name": "ALLBRANDS_117",
        "score": 0.13061446355268064
      },
      {
        "name": "ALLBRANDS_111",
        "score": 0.13061446355268064
      }
    ],
    "url": "https://www.wired.com/search/?q=sleep+rings+compared&sort=score+desc",
    "desc": "Search",
    "image": "https://www.wired.com/verso/static/wired/assets/newsletter-signup-hub.jpg",
    "keywords": {
      "list": [
        {
          "keyword": "wired",
          "score": 1
        },
        {
          "keyword": "matt simon",
          "score": 0.924532816468203
        },
        {
          "keyword": "condé nast",
          "score": 0.861198091844308
        },
        {
          "keyword": "david karpf",
          "score": 0.844018499335994
        },
        {
          "keyword": "gideon lichfield",
          "score": 0.8183791149770342
        },
        {
          "keyword": "paresh dave",
          "score": 0.7732257882376504
        },
        {
          "keyword": "vittoria elliott",
          "score": 0.7567044618651937
        },
        {
          "keyword": "lauren goode",
          "score": 0.732533211280936
        },
        {
          "keyword": "dell",
          "score": 0.6959032002175657
        },
        {
          "keyword": "laurence russell",
          "score": 0.6948466557905698
        },
        {
          "keyword": "simon hill",
          "score": 0.6438123451646943
        },
        {
          "keyword": "selena",
          "score": 0.6276396821723925
        },
        {
          "keyword": "cameron",
          "score": 0.5535192220415391
        },
        {
          "keyword": "jaina grey",
          "score": 0.5485522193972568
        },
        {
          "keyword": "jennifer m. wood",
          "score": 0.5427247584779192
        },
        {
          "keyword": "user agreement",
          "score": 0.5370151810285323
        },
        {
          "keyword": "privacy policy",
          "score": 0.5351589724844606
        },
        {
          "keyword": "you california privacy right",
          "score": 0.5314078376454013
        },
        {
          "keyword": "knight",
          "score": 0.5135969592634183
        },
        {
          "keyword": "michael calore",
          "score": 0.5070463382568331
        }
      ],
      "delimited": "wired|matt simon|condé nast|david karpf|gideon lichfield|paresh dave|vittoria elliott|lauren goode|dell|laurence russell|simon hill|selena|cameron|jaina grey|jennifer m. wood|user agreement|privacy policy|you california privacy right|knight|michael calore"
    },
    "entities": [
      {
        "name": "wired",
        "score": 1
      },
      {
        "name": "matt simon",
        "score": 0.924532816468203
      },
      {
        "name": "condé nast",
        "score": 0.861198091844308
      },
      {
        "name": "david karpf",
        "score": 0.844018499335994
      },
      {
        "name": "gideon lichfield",
        "score": 0.8183791149770342
      },
      {
        "name": "paresh dave",
        "score": 0.7732257882376504
      },
      {
        "name": "vittoria elliott",
        "score": 0.7567044618651937
      },
      {
        "name": "lauren goode",
        "score": 0.732533211280936
      },
      {
        "name": "dell",
        "score": 0.6959032002175657
      },
      {
        "name": "laurence russell",
        "score": 0.6948466557905698
      },
      {
        "name": "simon hill",
        "score": 0.6438123451646943
      },
      {
        "name": "selena",
        "score": 0.6276396821723925
      },
      {
        "name": "cameron",
        "score": 0.5535192220415391
      },
      {
        "name": "jaina grey",
        "score": 0.5485522193972568
      },
      {
        "name": "jennifer m. wood",
        "score": 0.5427247584779192
      },
      {
        "name": "user agreement",
        "score": 0.5370151810285323
      },
      {
        "name": "privacy policy",
        "score": 0.5351589724844606
      },
      {
        "name": "you california privacy right",
        "score": 0.5314078376454013
      },
      {
        "name": "knight",
        "score": 0.5135969592634183
      },
      {
        "name": "michael calore",
        "score": 0.5070463382568331
      }
    ],
    "pubdate": "1970-01-01T00:00:00.000+00:00",
    "title": "Search",
    "authors": [
      "condé nast"
    ]
  },
  "permutiveContextualCohorts": {},
  "payment": {
    "form": "free",
    "acceptableFormsOfTenderedPayment": [
      "free"
    ],
    "contentClassifiers": {
      "isPaywalled": false,
      "canBeSampled": false
    },
    "acceptableForms": [
      "free",
      "sample",
      "sub",
      "pass"
    ],
    "acceptableScopes": [
      "wired-adfree",
      "wired-adrich"
    ],
    "groupsToRender": [
      "ads",
      "consumer-marketing",
      "subscription-workflow"
    ],
    "entitlement": {
      "enabled": false,
      "domain": ".wired.com",
      "server": ""
    },
    "products": [
      {
        "name": "wired.com:adfree",
        "slug": "wiraf"
      },
      {
        "name": "wired.com:basic",
        "slug": "wir"
      }
    ],
    "negotiation": {
      "content": {
        "channelSlug": "search",
        "subChannelSlug": "",
        "contentType": "search",
        "functionalTags": [],
        "isPreview": false,
        "tags": []
      },
      "config": {
        "acceptableForms": [
          "free",
          "sample",
          "sub",
          "pass"
        ],
        "acceptableScopes": [
          "wired-adfree",
          "wired-adrich"
        ],
        "products": [
          {
            "name": "wired.com:adfree",
            "slug": "wiraf"
          },
          {
            "name": "wired.com:basic",
            "slug": "wir"
          }
        ],
        "contentTypes": [
          "article",
          "gallery"
        ],
        "renderingRules": [
          {
            "form": "free",
            "groups": [
              "ads",
              "consumer-marketing",
              "subscription-workflow"
            ]
          },
          {
            "form": "sample",
            "groups": [
              "ads",
              "consumer-marketing",
              "paywall",
              "subscription-workflow"
            ]
          },
          {
            "form": "sub",
            "groups": [
              "subs-cta"
            ]
          },
          {
            "form": "pass",
            "scope": "wired-adrich",
            "groups": [
              "ads",
              "subs-cta"
            ]
          },
          {
            "form": "pass",
            "scope": "wired-adfree",
            "groups": [
              "subs-cta"
            ]
          },
          {
            "form": "",
            "groups": [
              "ads",
              "consumer-marketing",
              "paywall",
              "subscription-workflow"
            ]
          }
        ],
        "entitlementChecks": {
          "sample": [
            "google"
          ],
          "free": [
            "google"
          ],
          "": [
            "google"
          ]
        },
        "allContentIsFree": false,
        "articlesAreFreeWhen": [
          {
            "tagged": "wired free access"
          }
        ]
      }
    },
    "bypass": true
  },
  "response": {
    "headers": {}
  },
  "paywall": {
    "strategy": "alpha",
    "paragraphLimit": 1,
    "gallerySlideLimit": 0,
    "isMuted": false,
    "gateway": {}
  },
  "databricks": {
    "enabled": false
  },
  "access": {
    "accessCondeBaseUrl": "https://access.conde.io/",
    "isAccessNegotiationEnabled": false,
    "contentRestricted": false,
    "reason": ""
  },
  "coreDataLayer": {
    "content": {
      "brand": "WIRED",
      "brandSlug": "wired",
      "contentLength": "all",
      "contentLang": "en-US",
      "contentSource": "web",
      "contentType": "search",
      "contentTitle": "Search",
      "dataSource": "web",
      "embeddedMedia": "",
      "functionalTags": "",
      "hasBuyButtons": "false",
      "pageValue": "all",
      "section": "search",
      "subsection": "",
      "subsection2": "",
      "tags": "search",
      "wordCount": "",
      "totalGalleryImages": "0"
    },
    "marketing": {
      "brand": "Wired"
    },
    "page": {
      "canonical": "https://www.wired.com/search/"
    },
    "search": {},
    "site": {
      "orgId": "4gKgcErvvpkwWft3fSWg7c2niGQB",
      "orgAppId": "a61a3c7a-01d9-4175-8ab8-7171949de605",
      "appVersion": "multi-tenant",
      "env": "production"
    },
    "syndication": {
      "content": "false",
      "originalSource": ""
    }
  },
  "googleTagManagerId": "5HBJC2K",
  "boomerang": {
    "tags": {
      "brand": "wired",
      "contentType": "search",
      "brand_slug": "wired",
      "content_type": "search"
    }
  },
  "brandName": "WIRED",
  "channelSlug": "default",
  "universalLayout": "default",
  "scTheme": {
    "colors": {
      "background": {
        "adContainer": {
          "inverted": "a2",
          "special": "c5",
          "standard": "g17",
          "sticky": "a3"
        },
        "black": "c1",
        "brand": "b2",
        "dark": "c1",
        "light": "c5",
        "white": "a3"
      },
      "consumption": {
        "body": {
          "inverted": {
            "accent": "b2",
            "adlabel": "g16",
            "bg-card": "a2",
            "bg-photo": "a2",
            "body": "c4",
            "body-deemphasized": "c3",
            "display-signature": "c4",
            "display-texture": "c4",
            "divider": "a2",
            "link": "c4",
            "link-hover": "a3",
            "subhed": "c4"
          },
          "special": {
            "accent": "b2",
            "adlabel": "g16",
            "bg-card": "c5",
            "bg-photo": "c5",
            "body": "c1",
            "body-deemphasized": "c2",
            "display-signature": "c1",
            "display-texture": "c1",
            "divider": "c4",
            "link": "c1",
            "link-hover": "b2",
            "subhed": "c1"
          },
          "standard": {
            "accent": "b2",
            "adlabel": "g16",
            "bg-card": "a3",
            "bg-photo": "c5",
            "body": "c1",
            "body-deemphasized": "c2",
            "display-signature": "c1",
            "display-texture": "c1",
            "divider": "c4",
            "link": "c1",
            "link-hover": "b2",
            "subhed": "c1"
          }
        },
        "lead": {
          "inverted": {
            "accent": "c4",
            "accreditation": "a3",
            "background": "a1",
            "context-signature": "a3",
            "context-tertiary": "a3",
            "context-texture": "a1",
            "description": "a3",
            "divider": "a2",
            "heading": "a3",
            "heading-background": "a1",
            "link": "a3",
            "link-hover": "c3",
            "syndication": "c3"
          },
          "special": {
            "accent": "a2",
            "accreditation": "a1",
            "background": "a3",
            "context-signature": "a2",
            "context-tertiary": "c2",
            "context-texture": "a3",
            "description": "a2",
            "divider": "c4",
            "heading": "a1",
            "heading-background": "a3",
            "link": "a1",
            "link-hover": "b2",
            "syndication": "c2"
          },
          "standard": {
            "accent": "a2",
            "accreditation": "a1",
            "background": "a3",
            "context-signature": "a1",
            "context-tertiary": "a1",
            "context-texture": "a3",
            "description": "a2",
            "divider": "c4",
            "heading": "a1",
            "heading-background": "a3",
            "link": "c1",
            "link-hover": "b2",
            "syndication": "a2"
          }
        }
      },
      "discovery": {
        "body": {
          "black": {
            "accent": "b2",
            "accreditation": "a3",
            "background": "c1",
            "border": "a2",
            "context-signature": "a3",
            "context-tertiary": "c4",
            "context-texture": "c1",
            "description": "c5",
            "divider": "a2",
            "heading": "a3",
            "heading-background": "c1",
            "syndication": "c4"
          },
          "brand": {
            "accent": "c1",
            "accreditation": "c1",
            "background": "c5",
            "border": "c4",
            "context-signature": "a2",
            "context-tertiary": "a2",
            "context-texture": "a3",
            "description": "a2",
            "divider": "c4",
            "heading": "a1",
            "heading-background": "a3",
            "syndication": "c2"
          },
          "dark": {
            "accent": "b2",
            "accreditation": "a3",
            "background": "c1",
            "border": "a2",
            "context-signature": "a3",
            "context-tertiary": "c4",
            "context-texture": "c1",
            "description": "c5",
            "divider": "a2",
            "heading": "a3",
            "heading-background": "c1",
            "syndication": "c4"
          },
          "light": {
            "accent": "b2",
            "accreditation": "c1",
            "background": "c5",
            "border": "c4",
            "context-signature": "a2",
            "context-tertiary": "a1",
            "context-texture": "a3",
            "description": "a2",
            "divider": "c4",
            "heading": "a1",
            "heading-background": "a3",
            "syndication": "c2"
          },
          "white": {
            "accent": "b2",
            "accreditation": "c1",
            "background": "a3",
            "border": "c4",
            "context-signature": "a2",
            "context-tertiary": "a1",
            "context-texture": "a3",
            "description": "a2",
            "divider": "c4",
            "heading": "a1",
            "heading-background": "a3",
            "syndication": "c2"
          }
        },
        "lead": {
          "primary": {
            "accent": "b2",
            "background": "a3",
            "description": "a2",
            "divider": "c4",
            "hed": "a1",
            "link": "a2",
            "link-hover": "b2"
          },
          "secondary": {
            "accent": "b2",
            "background": "c1",
            "description": "c4",
            "divider": "a2",
            "hed": "a3",
            "link": "c4",
            "link-hover": "a3"
          }
        }
      },
      "foundation": {
        "ad": {
          "background-inverted": "ad2",
          "background-standard": "ad1",
          "label-inverted": "ad4",
          "label-standard": "ad3"
        },
        "collapsed-menu": {
          "nav-link": {
            "default": "a1",
            "hover": "b2"
          },
          "utility-link": {
            "default": "a1",
            "hover": "b2"
          }
        },
        "expanded-context": "a2",
        "expanded-menu": {
          "nav-link": {
            "default": "a1",
            "hover": "b2"
          },
          "utility-link": {
            "default": "a1",
            "hover": "b2"
          }
        },
        "expanded-utility": {
          "nav-link": {
            "default": "a2",
            "hover": "b2"
          }
        },
        "footer": {
          "accent": "a2",
          "bg": "a1",
          "context": "c4",
          "links": {
            "primary": "c3",
            "secondary": "c2"
          },
          "meta-primary": "c5",
          "meta-secondary": "c2",
          "social": {
            "hover": "c4"
          }
        },
        "icon": {
          "default": "a2",
          "hover": "b2"
        },
        "menu": {
          "dividers": "c4"
        },
        "menu-bg": {
          "accent": "a3",
          "collapsed": "a3",
          "expanded": "a3"
        }
      },
      "interactive": {
        "base": {
          "black": "a1",
          "body": "a1",
          "border": "c3",
          "brand-primary": "b2",
          "brand-secondary": "c2",
          "dark": "c2",
          "deemphasized": "c2",
          "highlight": "c5",
          "light": "c2",
          "white": "a3",
          "hover": "hover1"
        },
        "feedback": {
          "alert-primary": "a3",
          "alert-secondary": "e2",
          "invalid-primary": "e2",
          "invalid-secondary": "a3",
          "notice-primary": "notice1",
          "notice-secondary": "notice2",
          "valid-primary": "a2",
          "valid-secondary": "c4"
        },
        "social": {
          "primary": "a1",
          "primary-hover": "a2",
          "secondary": "a3",
          "secondary-hover": "a3"
        }
      },
      "palette": {
        "a1": "rgba(0,0,0,1)",
        "a2": "rgba(51,51,51,1)",
        "a3": "rgba(255,255,255,1)",
        "a4": "rgba(233,103,0,1)",
        "ad1": "rgba(0,0,0,0.07000000029802322)",
        "ad2": "rgba(255,255,255,0.10000000149011612)",
        "ad3": "rgba(26,26,26,1)",
        "ad4": "rgba(247,247,247,1)",
        "b1": "rgba(0,197,89,1)",
        "b2": "rgba(5,125,188,1)",
        "b3": "rgba(208,229,230,1)",
        "b4": "rgba(255,192,53,1)",
        "b5": "rgba(35,25,39,1)",
        "c1": "rgba(26,26,26,1)",
        "c2": "rgba(117,117,117,1)",
        "c3": "rgba(153,153,153,1)",
        "c4": "rgba(229,229,229,1)",
        "c5": "rgba(243,243,243,1)",
        "e1": "rgba(41,133,82,1)",
        "e2": "rgba(235,0,0,1)",
        "g12": "rgba(69,145,194,1)",
        "g13": "rgba(59,89,152,1)",
        "g14": "rgba(0,123,182,1)",
        "g15": "rgba(189,8,28,1)",
        "g16": "rgba(151,151,151,1)",
        "g17": "rgba(255,255,255,0)",
        "notice1": "rgba(247,196,66,1)",
        "notice2": "rgba(255,242,208,1)",
        "hover1": "rgba(222, 235, 255, 1)"
      }
    },
    "container-styles": {
      "block-background": {
        "pattern": [
          {
            "solid": {
              "color": "#FFFFFF"
            }
          }
        ]
      },
      "content-background": null,
      "item-background": null,
      "lede-background": null,
      "main-background": null,
      "page-background": {
        "pattern": [
          {
            "solid": {
              "color": "#FFFFFF"
            }
          }
        ]
      }
    },
    "decorations": {
      "borderRadius": 0,
      "borderStyle": "solid",
      "borderWidth": 1,
      "cardRadiusLg": 0,
      "cardRadiusMd": 0,
      "cardRadiusSm": 0,
      "dividerStyle": "solid",
      "dividerWidth": 2,
      "iconProfileRadius": 0,
      "navigationRuleStyle": "solid",
      "navigationRuleWidth": 1,
      "sectionOrnamentLength": 50,
      "sectionOrnamentStyle": "solid",
      "sectionOrnamentWidth": 1,
      "titleBorderDecoration": {
        "type": "none",
        "file": "",
        "thickness": 0,
        "offset": 0,
        "placement": "grid",
        "repeat": "round",
        "width": "100%",
        "align": "center",
        "side": "bottom"
      },
      "sectionBorderPrimary": {
        "type": "none",
        "file": "",
        "thickness": 0,
        "offset": 0,
        "placement": "grid",
        "repeat": "round",
        "width": "100%",
        "align": "center",
        "side": "bottom"
      },
      "sectionBorderSecondary": {
        "type": "none",
        "file": "",
        "thickness": 0,
        "offset": 0,
        "placement": "grid",
        "repeat": "round",
        "width": "100%",
        "align": "center",
        "side": "bottom"
      },
      "sectionBorderTertiary": {
        "type": "none",
        "file": "",
        "thickness": 0,
        "offset": 0,
        "placement": "grid",
        "repeat": "round",
        "width": "100%",
        "align": "center",
        "side": "bottom"
      },
      "badgeFlagLg": {
        "file": "",
        "height": 0,
        "offsetX": 0,
        "offsetY": 0,
        "placement": "center",
        "rotation": 0,
        "type": "none",
        "width": 0,
        "x": "start",
        "y": "start"
      },
      "badgeFlagMd": {
        "file": "",
        "height": 0,
        "offsetX": 0,
        "offsetY": 0,
        "placement": "center",
        "rotation": 0,
        "type": "none",
        "width": 0,
        "x": "start",
        "y": "start"
      },
      "badgeFlagSm": {
        "file": "g",
        "height": 0,
        "offsetX": 0,
        "offsetY": 0,
        "placement": "center",
        "rotation": 0,
        "type": "none",
        "width": 0,
        "x": "start",
        "y": "start"
      },
      "badgePrimaryLg": {
        "file": "",
        "height": 0,
        "offsetX": 0,
        "offsetY": 0,
        "placement": "center",
        "rotation": 0,
        "type": "none",
        "width": 0,
        "x": "start",
        "y": "start"
      },
      "badgePrimaryMd": {
        "file": "",
        "height": 0,
        "offsetX": 0,
        "offsetY": 0,
        "placement": "center",
        "rotation": 0,
        "type": "none",
        "width": 0,
        "x": "start",
        "y": "start"
      },
      "badgePrimarySm": {
        "file": "",
        "height": 0,
        "offsetX": 0,
        "offsetY": 0,
        "placement": "center",
        "rotation": 0,
        "type": "none",
        "width": 0,
        "x": "start",
        "y": "start"
      },
      "badgeSecondaryLg": {
        "file": "",
        "height": 0,
        "offsetX": 0,
        "offsetY": 0,
        "placement": "center",
        "rotation": 0,
        "type": "none",
        "width": 0,
        "x": "start",
        "y": "start"
      },
      "badgeSecondaryMd": {
        "file": "",
        "height": 0,
        "offsetX": 0,
        "offsetY": 0,
        "placement": "center",
        "rotation": 0,
        "type": "none",
        "width": 0,
        "x": "start",
        "y": "start"
      },
      "badgeSecondarySm": {
        "file": "",
        "height": 0,
        "offsetX": 0,
        "offsetY": 0,
        "placement": "center",
        "rotation": 0,
        "type": "none",
        "width": 0,
        "x": "start",
        "y": "start"
      },
      "backgroundImagePrimary": {
        "type": "none",
        "file": "",
        "attachment": "initial",
        "position": "initial",
        "repeat": "no-repeat",
        "size": "cover"
      },
      "backgroundImageSecondary": {
        "type": "none",
        "file": "",
        "attachment": "initial",
        "position": "initial",
        "repeat": "no-repeat",
        "size": "cover"
      }
    },
    "interactive": {
      "links": {
        "default": {
          "active": {
            "style": "underline"
          },
          "focus": {
            "style": "underline"
          },
          "hover": {
            "style": "underline"
          },
          "link": {
            "style": "underline"
          },
          "visited": {
            "style": "underline"
          }
        },
        "navigation": {
          "active": {
            "style": "underline"
          },
          "focus": {
            "style": "underline"
          },
          "hover": {
            "style": "underline"
          },
          "link": {
            "style": "null"
          },
          "visited": {
            "style": "null"
          }
        }
      }
    },
    "navigation": {
      "header": {
        "container-spacing-unit": 0,
        "lg": {
          "align-logo": "left",
          "hasPrimary": false,
          "hasSecondary": true,
          "logo-height": 3.25,
          "logo-padding": [
            0,
            3
          ]
        },
        "max-width": 1280,
        "md": {
          "align-logo": "left",
          "hasPrimary": false,
          "hasSecondary": true,
          "logo-height": 3.25,
          "logo-padding": [
            0,
            3
          ]
        },
        "sm": {
          "align-logo": "center",
          "hasPrimary": false,
          "hasSecondary": true,
          "logo-height": 2,
          "logo-padding": [
            0,
            3
          ]
        },
        "xl": {
          "align-logo": "left",
          "hasPrimary": true,
          "hasSecondary": true,
          "logo-height": 3,
          "logo-padding": [
            0,
            3
          ]
        }
      }
    },
    "spacing": {
      "box-inset": 10,
      "spacing-0": "0px",
      "spacing-4": "4px",
      "spacing-8": "8px",
      "spacing-12": "12px",
      "spacing-16": "16px",
      "spacing-24": "24px",
      "spacing-32": "32px",
      "spacing-40": "40px",
      "spacing-48": "48px",
      "spacing-56": "56px",
      "spacing-64": "64px",
      "spacing-96": "96px",
      "spacing-128": "128px",
      "section": {
        "gap-sm": "spacing-0",
        "gap-md": "spacing-0",
        "padding-top-sm": "spacing-0",
        "padding-top-md": "spacing-0",
        "padding-bottom-sm": "spacing-0",
        "padding-bottom-md": "spacing-0"
      }
    },
    "motion": {
      "duration": {
        "0": "0ms",
        "100": "100ms",
        "150": "150ms",
        "200": "200ms",
        "250": "250ms",
        "300": "300ms",
        "400": "400ms",
        "500": "500ms",
        "800": "800ms",
        "1200": "1200ms"
      },
      "delay": {
        "50": "0ms",
        "100": "100ms",
        "150": "150ms",
        "200": "200ms",
        "250": "250ms",
        "300": "300ms",
        "400": "400ms",
        "500": "500ms",
        "700": "700ms"
      },
      "easing": {
        "linear": "0,0,1,1",
        "standard-in-and-out": "0.37,0,0.63,1",
        "standard-in": "0.12,0,0.39,0",
        "standard-out": "0.61,1,0.88,1",
        "emphasized-in-and-out": "0.65,0,0.35,1",
        "emphasized-in": "0.32,0,0.67,0",
        "emphasized-out": "0.33,1,0.68,1",
        "playful-in-and-out": "0.83,0,0.17,1",
        "playful-in": "0.64,0,0.78,0",
        "playful-out": "0.22,1,0.36,1"
      },
      "pattern": {
        "move": {
          "easing": "standard-in-and-out",
          "duration": "duration.200"
        },
        "move-enter": {
          "easing": "standard-in-and-out",
          "duration": "duration.200"
        },
        "move-exit": {
          "easing": "standard-in-and-out",
          "duration": "duration.200"
        },
        "fade-in-instant": {
          "easing": "standard-in-and-out",
          "duration": "duration.0"
        },
        "fade-in-medium": {
          "easing": "standard-in-and-out",
          "duration": "duration.300"
        },
        "fade-out-medium": {
          "easing": "standard-in-and-out",
          "duration": "duration.300"
        },
        "collapse": {
          "easing": "standard-in-and-out",
          "duration": "duration.300"
        },
        "expand": {
          "easing": "emphasized-in-and-out",
          "duration": "duration.400"
        },
        "spin": {
          "easing": "linear",
          "duration": "duration.1200"
        },
        "rotate180": {
          "easing": "emphasized-in-and-out",
          "duration": "duration.400"
        }
      }
    },
    "typography": {
      "definitions": {
        "commerce": {
          "brand-name": {
            "case": "normal",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.25,
            "mobile-size": 16,
            "weight": 400
          },
          "call-to-action": {
            "case": "uppercase",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": 0.10000000397364299,
            "ligatures": null,
            "line-height": 1.3300000031789143,
            "mobile-size": 12,
            "weight": 700
          },
          "label": {
            "case": "normal",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3333333333333333,
            "mobile-size": 12,
            "weight": 700
          },
          "product-description": {
            "case": "normal",
            "family": "BreveText",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3333333333333333,
            "mobile-size": 18,
            "weight": 400
          },
          "product-title": {
            "case": "normal",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3333333333333333,
            "mobile-size": 18,
            "weight": 700
          }
        },
        "consumptionEditorial": {
          "body-core": {
            "case": "normal",
            "family": "BreveText",
            "italic": false,
            "letter-spacing": 0.005684210673758858,
            "ligatures": null,
            "line-height": 1.4736842105263157,
            "mobile-size": 19,
            "weight": 400
          },
          "body-feature": {
            "case": "normal",
            "family": "BreveText",
            "italic": false,
            "letter-spacing": 0.005385041629013263,
            "ligatures": null,
            "line-height": 1.4736842105263157,
            "mobile-size": 19,
            "weight": 400
          },
          "citation": {
            "case": "normal",
            "family": "BreveText",
            "italic": false,
            "letter-spacing": 0.005599999924500784,
            "ligatures": null,
            "line-height": 1.3333333333333333,
            "mobile-size": 15,
            "weight": 400
          },
          "description-core": {
            "case": "normal",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": 0.006000000238418579,
            "ligatures": null,
            "line-height": 1.4,
            "mobile-size": 20,
            "weight": 700
          },
          "description-embed": {
            "case": "normal",
            "family": "BreveText",
            "fontSizeMd": 16,
            "italic": false,
            "letter-spacing": 0.005625000223517418,
            "ligatures": null,
            "line-height": 1.5,
            "lineHeightMd": 1.5,
            "mobile-size": 16,
            "weight": 400
          },
          "description-feature": {
            "case": "normal",
            "family": "BreveText",
            "italic": false,
            "letter-spacing": 0.005999999919107982,
            "ligatures": null,
            "line-height": 1.2857142857142858,
            "mobile-size": 28,
            "weight": 400
          },
          "display-large": {
            "case": "normal",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": -0.02647058928714079,
            "ligatures": null,
            "line-height": 1,
            "mobile-size": 34,
            "weight": 700
          },
          "display-medium": {
            "case": "normal",
            "family": "BreveText",
            "italic": false,
            "letter-spacing": -0.031071428741727556,
            "ligatures": null,
            "line-height": 1.1428571428571428,
            "mobile-size": 28,
            "weight": 300
          },
          "display-small": {
            "case": "normal",
            "family": "BreveText",
            "fontSizeMd": 28,
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3333333333333333,
            "lineHeightMd": 1.2857142857142858,
            "mobile-size": 24,
            "weight": 400
          },
          "hed-bulletin": {
            "case": "normal",
            "family": "Apercu",
            "fontSizeMd": 24,
            "italic": false,
            "letter-spacing": -0.013999999811251959,
            "ligatures": null,
            "line-height": 1.3333333333333333,
            "lineHeightMd": 1.3333333333333333,
            "mobile-size": 24,
            "weight": 700
          },
          "hed-feature": {
            "case": "normal",
            "family": "WiredDisplay",
            "fontSizeLg": 60,
            "fontSizeMd": 52,
            "italic": false,
            "letter-spacing": -0.011363636363636364,
            "ligatures": null,
            "line-height": 1.0909090909090908,
            "lineHeightLg": 1,
            "lineHeightMd": 1.0769230769230769,
            "mobile-size": 44,
            "weight": 400
          },
          "hed-standard": {
            "case": "normal",
            "family": "WiredDisplay",
            "fontSizeLg": 54,
            "fontSizeMd": 44,
            "italic": false,
            "letter-spacing": -0.01326315810805873,
            "ligatures": null,
            "line-height": 1.0526315789473684,
            "lineHeightLg": 1.037037037037037,
            "lineHeightMd": 1.0909090909090908,
            "mobile-size": 38,
            "weight": 400
          },
          "subhed-aux-primary": {
            "case": "normal",
            "family": "ProximaNova",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.2,
            "mobile-size": 20,
            "weight": 700
          },
          "subhed-aux-secondary": {
            "case": "normal",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.25,
            "mobile-size": 16,
            "weight": 700
          },
          "subhed-break-primary": {
            "case": "normal",
            "family": "Apercu",
            "fontSizeMd": 34,
            "italic": false,
            "letter-spacing": -0.01650000044277736,
            "ligatures": null,
            "line-height": 1.2857142857142858,
            "lineHeightMd": 1.1764705882352942,
            "mobile-size": 28,
            "weight": 700
          },
          "subhed-break-secondary": {
            "case": "normal",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": -0.016333332906166714,
            "ligatures": null,
            "line-height": 1.1666666666666667,
            "mobile-size": 24,
            "weight": 700
          }
        },
        "discovery": {
          "description-core": {
            "case": "normal",
            "family": "BreveText",
            "italic": false,
            "letter-spacing": 0.005625000223517418,
            "ligatures": null,
            "line-height": 1.5,
            "mobile-size": 16,
            "weight": 400
          },
          "description-feature": {
            "case": "normal",
            "family": "BreveText",
            "fontSizeMd": 18,
            "italic": false,
            "letter-spacing": 0.004999999888241291,
            "ligatures": null,
            "line-height": 1.5,
            "lineHeightMd": 1.3333333333333333,
            "mobile-size": 16,
            "weight": 400
          },
          "description-page": {
            "case": "normal",
            "family": "BreveText",
            "fontSizeMd": 18,
            "italic": false,
            "letter-spacing": 0.006000000052154064,
            "ligatures": null,
            "line-height": 1.375,
            "lineHeightMd": 1.3333333333333333,
            "mobile-size": 16,
            "weight": 400
          },
          "hed-break-out": {
            "case": "normal",
            "family": "WiredDisplay",
            "fontSizeLg": 48,
            "fontSizeMd": 48,
            "italic": false,
            "letter-spacing": -0.011363636363636364,
            "ligatures": null,
            "line-height": 1,
            "lineHeightLg": 1,
            "lineHeightMd": 1,
            "mobile-size": 44,
            "weight": 400
          },
          "hed-bulletin-primary": {
            "case": "normal",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": -0.008470587870653938,
            "ligatures": null,
            "line-height": 1.2941176470588236,
            "mobile-size": 17,
            "weight": 700
          },
          "hed-bulletin-secondary": {
            "case": "normal",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.2941176470588236,
            "mobile-size": 17,
            "weight": 700
          },
          "hed-core-primary": {
            "case": "normal",
            "family": "Apercu",
            "fontSizeMd": 20,
            "italic": false,
            "letter-spacing": -0.014000000059604644,
            "ligatures": null,
            "line-height": 1.2,
            "lineHeightMd": 1.2,
            "mobile-size": 20,
            "weight": 700
          },
          "hed-core-secondary": {
            "case": "normal",
            "family": "Apercu",
            "fontSizeMd": 20,
            "italic": false,
            "letter-spacing": -0.014000000059604644,
            "ligatures": null,
            "line-height": 1.2,
            "lineHeightMd": 1.2,
            "mobile-size": 20,
            "weight": 700
          },
          "hed-feature": {
            "case": "normal",
            "family": "WiredDisplay",
            "fontSizeLg": 56,
            "fontSizeMd": 52,
            "italic": false,
            "letter-spacing": -0.011363636363636364,
            "ligatures": null,
            "line-height": 1,
            "lineHeightLg": 1,
            "lineHeightMd": 1,
            "mobile-size": 44,
            "weight": 400
          },
          "page-hed-section": {
            "case": "normal",
            "family": "WiredDisplay",
            "fontSizeMd": 54,
            "italic": false,
            "letter-spacing": -0.013157894736842105,
            "ligatures": null,
            "line-height": 1.0526315789473684,
            "lineHeightMd": 1.037037037037037,
            "mobile-size": 38,
            "weight": 400
          },
          "page-hed-subsection": {
            "case": "normal",
            "family": "Apercu",
            "fontSizeMd": 48,
            "italic": false,
            "letter-spacing": -0.008470588747192831,
            "ligatures": null,
            "line-height": 1.1764705882352942,
            "lineHeightMd": 1.1666666666666667,
            "mobile-size": 34,
            "weight": 700
          },
          "subhed-section-collection": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0.04338461619157057,
            "ligatures": null,
            "line-height": 1.2307692307692308,
            "mobile-size": 13,
            "weight": 700
          },
          "subhed-section-primary": {
            "case": "uppercase",
            "family": "WiredMono",
            "fontSizeMd": 13,
            "italic": false,
            "letter-spacing": 0.06615384725423959,
            "ligatures": null,
            "line-height": 1.2307692307692308,
            "lineHeightMd": 1.2307692307692308,
            "mobile-size": 13,
            "weight": 400
          },
          "subhed-section-secondary": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0.04338461619157057,
            "ligatures": null,
            "line-height": 1.2276923106266902,
            "mobile-size": 13,
            "weight": 400
          },
          "subhed-section-tertiary": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.2307692307692308,
            "mobile-size": 13,
            "weight": 700
          }
        },
        "foundation": {
          "ad-label": {
            "case": "normal",
            "family": "Helvetica",
            "italic": false,
            "letter-spacing": 0.2,
            "ligatures": null,
            "line-height": 1.6,
            "mobile-size": 10,
            "weight": 400
          },
          "link-feature": {
            "case": "normal",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.1428571428571428,
            "mobile-size": 28,
            "weight": 700
          },
          "link-primary": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0.08333333513953468,
            "ligatures": null,
            "line-height": 1.4545454545454546,
            "mobile-size": 11,
            "weight": 400
          },
          "link-secondary": {
            "case": "normal",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3300000031789143,
            "mobile-size": 12,
            "weight": 400
          },
          "link-utility": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0.08333333513953468,
            "ligatures": null,
            "line-height": 1.4545454545454546,
            "mobile-size": 11,
            "weight": 400
          },
          "list": {
            "case": "normal",
            "family": "ProximaNova",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3333333333333333,
            "mobile-size": 12,
            "weight": 400
          },
          "meta-primary": {
            "case": "normal",
            "family": "BreveText",
            "italic": false,
            "letter-spacing": 0.005999999919107982,
            "ligatures": null,
            "line-height": 1.4300000326974052,
            "mobile-size": 14,
            "weight": 400
          },
          "meta-secondary": {
            "case": "normal",
            "family": "ProximaNova",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.4545454545454546,
            "mobile-size": 11,
            "weight": 400
          },
          "title-primary": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0.10000000397364299,
            "ligatures": null,
            "line-height": 1.3300000031789143,
            "mobile-size": 12,
            "weight": 400
          },
          "title-secondary": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0.10000000216744163,
            "ligatures": null,
            "line-height": 1.4545454545454546,
            "mobile-size": 11,
            "weight": 700
          }
        },
        "globalEditorial": {
          "accreditation-core": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3333333333333333,
            "mobile-size": 12,
            "weight": 400
          },
          "accreditation-feature": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3333333333333333,
            "mobile-size": 12,
            "weight": 400
          },
          "ad-label": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0.15,
            "ligatures": null,
            "line-height": 1,
            "mobile-size": 10,
            "weight": 400
          },
          "context-primary": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0.09166666865348816,
            "ligatures": null,
            "line-height": 1.3333333333333333,
            "mobile-size": 12,
            "weight": 400
          },
          "context-secondary": {
            "case": "normal",
            "family": "ProximaNova",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3300000031789143,
            "mobile-size": 12,
            "weight": 400
          },
          "context-tertiary": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0.04500000043348833,
            "ligatures": null,
            "line-height": 1.4545454545454546,
            "mobile-size": 11,
            "weight": 400
          },
          "context-title": {
            "case": "normal",
            "family": "ProximaNova",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3300000031789143,
            "mobile-size": 12,
            "weight": 700
          },
          "numerical-large": {
            "case": "normal",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.2857142857142858,
            "mobile-size": 28,
            "weight": 700
          },
          "numerical-small": {
            "case": "uppercase",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3300000031789143,
            "mobile-size": 12,
            "weight": 700
          },
          "syndication": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0.0625312477350235,
            "ligatures": null,
            "line-height": 1.5,
            "mobile-size": 16,
            "weight": 300
          },
          "tags": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0.04500000043348833,
            "ligatures": null,
            "line-height": 1.4545454545454546,
            "mobile-size": 11,
            "weight": 300
          }
        },
        "utility": {
          "assistive-text": {
            "case": "normal",
            "family": "ProximaNova",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3333333333333333,
            "mobile-size": 12,
            "weight": 400
          },
          "body": {
            "case": "normal",
            "family": "ProximaNova",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.2307692308,
            "mobile-size": 13,
            "weight": 400
          },
          "button-bulletin": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0.10000000216744163,
            "ligatures": null,
            "line-height": 1.1799999583851208,
            "mobile-size": 11,
            "weight": 400
          },
          "button-core": {
            "case": "uppercase",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": 0.10000000397364299,
            "ligatures": null,
            "line-height": 1.3300000031789143,
            "mobile-size": 12,
            "weight": 700
          },
          "button-utility": {
            "case": "uppercase",
            "family": "WiredMono",
            "italic": false,
            "letter-spacing": 0.10000000397364299,
            "ligatures": null,
            "line-height": 1.3300000031789143,
            "mobile-size": 12,
            "weight": 700
          },
          "card-heading": {
            "case": "normal",
            "family": "Apercu",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.2727272727272727,
            "mobile-size": 22,
            "weight": 700
          },
          "description": {
            "case": "normal",
            "family": "ProximaNova",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.2222222222222223,
            "mobile-size": 18,
            "weight": 400
          },
          "heading": {
            "case": "normal",
            "family": "Apercu",
            "fontSizeMd": 42,
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.125,
            "lineHeightMd": 1.2857142857142858,
            "mobile-size": 32,
            "weight": 700
          },
          "input-core": {
            "case": "normal",
            "family": "ProximaNova",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.25,
            "mobile-size": 16,
            "weight": 400
          },
          "input-feature": {
            "case": "normal",
            "family": "BreveText",
            "fontSizeMd": 34,
            "italic": false,
            "letter-spacing": 0.006000000052154064,
            "ligatures": null,
            "line-height": 1.25,
            "lineHeightMd": 1.1764705882352942,
            "mobile-size": 32,
            "weight": 400
          },
          "label": {
            "case": "normal",
            "family": "ProximaNova",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3300000031789143,
            "mobile-size": 12,
            "weight": 400
          },
          "landing-body": {
            "case": "normal",
            "family": "BreveText",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.411764705882353,
            "mobile-size": 17,
            "weight": 400
          },
          "landing-description": {
            "case": "normal",
            "family": "ProximaNova",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3333333333333333,
            "mobile-size": 18,
            "weight": 400
          },
          "landing-heading": {
            "case": "normal",
            "family": "Apercu",
            "fontSizeLg": 42,
            "fontSizeMd": 36,
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.2,
            "lineHeightLg": 1.2857142857142858,
            "lineHeightMd": 1.1111111111111112,
            "mobile-size": 30,
            "weight": 700
          },
          "landing-subheading": {
            "case": "normal",
            "family": "Apercu",
            "fontSizeMd": 32,
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.2857142857142858,
            "lineHeightMd": 1.25,
            "mobile-size": 28,
            "weight": 700
          },
          "list-heading": {
            "case": "normal",
            "family": "ProximaNova",
            "fontSizeMd": 16,
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 2,
            "lineHeightMd": 1.75,
            "mobile-size": 14,
            "weight": 400
          },
          "modal-body": {
            "case": "normal",
            "family": "BreveText",
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.5555555555555556,
            "mobile-size": 18,
            "weight": 400
          },
          "modal-hed": {
            "case": "normal",
            "family": "Apercu",
            "fontSizeMd": 30,
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.3333333333333333,
            "lineHeightMd": 1.3333333333333333,
            "mobile-size": 30,
            "weight": 700
          },
          "pricing": {
            "case": "normal",
            "family": "Apercu",
            "fontSizeMd": 22,
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1.4545454545454546,
            "lineHeightMd": 1.4545454545454546,
            "mobile-size": 22,
            "weight": 700
          },
          "pricing-secondary": {
            "case": "normal",
            "family": "Apercu",
            "fontSizeMd": 16,
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 2.2857142857142856,
            "lineHeightMd": 2,
            "mobile-size": 14,
            "weight": 400
          },
          "subheading": {
            "case": "normal",
            "family": "Apercu",
            "fontSizeMd": 24,
            "italic": false,
            "letter-spacing": 0,
            "ligatures": null,
            "line-height": 1,
            "lineHeightMd": 1.1666666666666667,
            "mobile-size": 18,
            "weight": 500
          }
        }
      },
      "typefaces": {
        "Apercu": {
          "fallback": "'helvetica, sans-serif'"
        },
        "BreveText": {
          "fallback": "'helvetica, sans-serif'"
        },
        "ProximaNova": {
          "fallback": "'helvetica, sans-serif'"
        },
        "WiredDisplay": {
          "fallback": "'helvetica, sans-serif'"
        },
        "WiredMono": {
          "fallback": "'helvetica, sans-serif'"
        },
        "Helvetica": {
          "fallback": "'helvetica, sans-serif'"
        },
        "Georgia": {
          "fallback": "'helvetica, sans-serif'"
        }
      },
      "fontFaces": "\n      \n  @font-face {\n    font-family: Apercu;\n    font-weight: 700;\n    font-style: normal;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/Apercu-Bold-Pro.woff2\") format(\"woff2\"), url(\"/verso/static/assets/fonts/Apercu-Bold-Pro.woff\") format(\"woff\"); \n  }\n    \n  @font-face { \n    font-family: Apercu;\n    font-weight: 400;\n    font-style: normal;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/Apercu-Regular-Pro.woff2\") format(\"woff2\"), url(\"/verso/static/assets/fonts/Apercu-Regular-Pro.woff\") format(\"woff\");\n  }\n\n      \n  @font-face { \n    font-family: BreveText;\n    font-weight: 700;\n    font-style: normal;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/BreveText-Bold.woff\") format(\"woff\");\n  }\n  \n  @font-face { \n    font-family: BreveText;\n    font-weight: 700;\n    font-style: italic;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/BreveText-BoldItalic.woff\") format(\"woff\");\n  }\n  \n  @font-face { \n    font-family: BreveText;\n    font-weight: 300;\n    font-style: normal;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/BreveText-Book.woff\") format(\"woff\");\n  }\n  \n  @font-face { \n    font-family: BreveText;\n    font-weight: 300;\n    font-style: italic;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/BreveText-BookItalic.woff\") format(\"woff\");\n  }\n  \n      \n  @font-face {\n    font-family: LabGrotesque;\n    font-weight: 900;\n    font-style: normal;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/LabGrotesque-Black.woff2\") format(\"woff2\"), url(\"/verso/static/assets/fonts/LabGrotesque-Black.woff\") format(\"woff\"); }\n\n  @font-face {\n    font-family: LabGrotesque;\n    font-weight: 700;\n    font-style: normal;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/LabGrotesque-Bold.woff2\") format(\"woff2\"), url(\"/verso/static/assets/fonts/LabGrotesque-Bold.woff\") format(\"woff\"); }\n\n  @font-face {\n    font-family: LabGrotesque;\n    font-weight: 500;\n    font-style: normal;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/LabGrotesque-Medium.woff2\") format(\"woff2\"), url(\"/verso/static/assets/fonts/LabGrotesque-Medium.woff\") format(\"woff\"); }\n\n      \n  @font-face {\n    font-family: ProximaNova;\n    font-weight: 700;\n    font-style: normal;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/ProximaNova-Bold.woff2\") format(\"woff2\"), url(\"/verso/static/assets/fonts/ProximaNova-Bold.woff\") format(\"woff\"); }\n\n  @font-face { \n    font-family: ProximaNova;\n    font-weight: 400;\n    font-style: normal;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/ProximaNova-Regular.woff\") format(\"woff\");\n  }\n  \n  @font-face { \n    font-family: ProximaNova;\n    font-weight: 400;\n    font-style: italic;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/ProximaNova-RegularItalic.woff\") format(\"woff\");\n  }\n  \n      \n  @font-face { \n    font-family: WiredDisplay;\n    font-weight: 700;\n    font-style: normal;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/WiredDisplay-BoldCondensed.woff\") format(\"woff\");\n  }\n  @font-face { \n    font-family: WiredDisplay;\n    font-weight: 400;\n    font-style: normal;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/WiredDisplayVF.woff2\") format(\"woff2\"), url(\"/verso/static/assets/fonts/WiredDisplayVF.woff\") format(\"woff\");\n  }\n  @font-face { \n    font-family: WiredDisplay;\n    font-weight: 400;\n    font-style: italic;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/WiredDisplay-BoldCondensedItalic.woff\") format(\"woff\");\n  }\n    \n      \n  @font-face { \n    font-family: WiredMono;\n    font-weight: 700;\n    font-style: normal;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/WiredMono-Bold.woff\") format(\"woff\");\n  }\n  \n  @font-face { \n    font-family: WiredMono;\n    font-weight: 300;\n    font-style: normal;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/WiredMono-Light.woff\") format(\"woff\");\n  }\n  \n  @font-face { \n    font-family: WiredMono;\n    font-weight: 400;\n    font-style: normal;\n    font-display: swap;\n    src: url(\"/verso/static/assets/fonts/WiredMono-Regular.woff2\") format(\"woff2\"), url(\"/verso/static/assets/fonts/WiredMono-Regular.woff\") format(\"woff\");\n  }\n    "
    },
    "meta": {
      "name": "wired-us",
      "market": "us"
    }
  },
  "presenter": "presenter-search",
  "comScoreCollectionName": "",
  "footerLogo": {
    "altText": "WIRED",
    "sources": {
      "sm": {
        "url": "/verso/static/wired-us/assets/logo-reverse.svg"
      }
    }
  },
  "headerLogo": {
    "altText": "WIRED",
    "sources": {
      "sm": {
        "url": "/verso/static/wired-us/assets/logo-header.svg"
      }
    }
  },
  "headerInvertedLogo": {
    "altText": "WIRED",
    "sources": {
      "sm": {
        "url": "/verso/static/wired-us/assets/logo-reverse.svg"
      }
    }
  },
  "logo": {
    "altText": "WIRED",
    "sources": {
      "sm": {
        "url": "/verso/static/wired-us/assets/logo.svg"
      }
    }
  },
  "invertedLogo": {
    "altText": "WIRED",
    "sources": {
      "sm": {
        "url": "/verso/static/wired-us/assets/logo-reverse.svg"
      }
    }
  },
  "logoBaseUrl": "/",
  "head.og.image": "https://www.wired.com/verso/static/wired-us/assets/newsletter-signup-hub.jpg",
  "rootBrandName": "Wired",
  "head.twitterImageSrc": "https://www.wired.com/verso/static/wired-us/assets/newsletter-signup-hub.jpg",
  "seriesLogos": {},
  "snowplow": {
    "collectorURL": "https://www.wired.com",
    "enableSnowplow": true,
    "slug": "wired",
    "appInfoObj": {
      "appName": "Verso",
      "appEnv": "production",
      "appVersion": "9146"
    }
  },
  "fourd": {
    "enableFourdUser": true
  },
  "legalese": {},
  "landingPageLink": {},
  "navigationSearch": true,
  "translations": {
    "AccountInformationCard.Discard": [
      {
        "type": 0,
        "value": "Discard"
      }
    ],
    "AccountInformationCard.ErrorMessage": [
      {
        "type": 0,
        "value": "Unable to save username. Please try again."
      }
    ],
    "AccountInformationCard.SubmitButtonLabel": [
      {
        "type": 0,
        "value": "Save Username"
      }
    ],
    "AccountInformationCard.SuccessMessage": [
      {
        "type": 0,
        "value": "Your username is saved."
      }
    ],
    "AccountInformationCard.UserNameLabel": [
      {
        "type": 0,
        "value": "Username"
      }
    ],
    "AccountInformationCard.UserNamePlaceholer": [
      {
        "type": 0,
        "value": "YOUR_USERNAME"
      }
    ],
    "AccountInformationCard.alreadyTakenError": [
      {
        "type": 0,
        "value": "This Username is already taken."
      }
    ],
    "AccountInformationCard.lengthError": [
      {
        "type": 0,
        "value": "Usernames must be between 2 and 23 characters."
      }
    ],
    "AccountInformationCard.specialCharError": [
      {
        "type": 0,
        "value": "Usernames can only include letters, numbers and underscores (_)."
      }
    ],
    "AccountLinks.NavigationAriaLabel": [
      {
        "type": 0,
        "value": "Account"
      }
    ],
    "Ad.adLabel": [
      {
        "type": 0,
        "value": "Advertisement"
      }
    ],
    "AgeGate.AcceptLabel": [
      {
        "type": 0,
        "value": "I am 18+"
      }
    ],
    "AgeGate.DeclineLabel": [
      {
        "type": 0,
        "value": "I'm under 18"
      }
    ],
    "AgeGate.DekText": [
      {
        "type": 0,
        "value": "This material is intended for people over the age of 18"
      }
    ],
    "AgeGate.HedText": [
      {
        "type": 0,
        "value": "Are you 18 or over?"
      }
    ],
    "ArticlePage.Back to article": [
      {
        "type": 0,
        "value": "Back to article"
      }
    ],
    "ArticlePage.DefaultDisclaimer": [
      {
        "type": 0,
        "value": "All products are independently selected by our editors. If you buy something, we may earn an affiliate commission."
      }
    ],
    "ArticlePage.From the issue of": [
      {
        "type": 0,
        "value": "From the issue of"
      }
    ],
    "ArticlePage.TruncatedButtonLabel": [
      {
        "type": 0,
        "value": "Read Full Story"
      }
    ],
    "AudioPrimaryLabel.Listen": [
      {
        "type": 0,
        "value": "Listen"
      }
    ],
    "AudioSecondaryLabel.NowPlaying": [
      {
        "type": 0,
        "value": "Now playing"
      }
    ],
    "BizzaboEmbed.ConsentBannerHeader": [
      {
        "type": 0,
        "value": "Bizzabo content"
      }
    ],
    "BlueskyEmbed.AriaLabelText": [
      {
        "type": 0,
        "value": "social media post"
      }
    ],
    "BlueskyEmbed.ConsentBannerHeader": [
      {
        "type": 0,
        "value": "Bluesky content"
      }
    ],
    "Bookmark.SignInMessage": [
      {
        "type": 0,
        "value": "After signing in, you can save stories and easily revisit them on any device—even off-line."
      }
    ],
    "BookmarkButton.Label": [
      {
        "type": 0,
        "value": "save recipe"
      }
    ],
    "BookmarkButton.LabelSaved": [
      {
        "type": 0,
        "value": "recipe saved"
      }
    ],
    "BookmarkIcon.Alert": [
      {
        "type": 0,
        "value": "Save this story for later."
      }
    ],
    "BookmarkIcon.CompletionLabel": [
      {
        "type": 0,
        "value": "Story saved. To revisit this article, select My Account, then View Saved Stories. Press Escape to dismiss tooltip."
      }
    ],
    "BookmarkIcon.Label": [
      {
        "type": 0,
        "value": "Story saved"
      }
    ],
    "BookmarkIcon.OnboardingAriaLabel": [
      {
        "type": 0,
        "value": "Save story. Press Enter to save this story for later. Press Escape to dismiss tooltip."
      }
    ],
    "BookmarkIcon.SignInMessage": [
      {
        "type": 0,
        "value": "After signing in, you can save stories and easily revisit them on any device—even off-line."
      }
    ],
    "BookmarkPrimaryLabel.RecipeSaved": [
      {
        "type": 0,
        "value": "Recipe Saved"
      }
    ],
    "BookmarkPrimaryLabel.Save": [
      {
        "type": 0,
        "value": "Save"
      }
    ],
    "BookmarkPrimaryLabel.SaveRecipe": [
      {
        "type": 0,
        "value": "Save Recipe"
      }
    ],
    "BookmarkPrimaryLabel.SaveThisStory": [
      {
        "type": 0,
        "value": "Save this story"
      }
    ],
    "BookmarkPrimaryLabel.Saved": [
      {
        "type": 0,
        "value": "Saved"
      }
    ],
    "BookmarkPrimaryLabel.SavedToLibrary": [
      {
        "type": 0,
        "value": "Saved to library"
      }
    ],
    "BusinessApplication.AccountProfileIsResubmittedText": [
      {
        "type": 0,
        "value": "Updated"
      }
    ],
    "BusinessApplication.AccountProfileLink": [
      {
        "type": 1,
        "value": "url"
      }
    ],
    "BusinessApplication.ApplicationAPIErrorMessage": [
      {
        "type": 0,
        "value": "We couldn't complete this. Please try again."
      }
    ],
    "BusinessApplication.ApplicationBannerDeletePhotoLabel": [
      {
        "type": 0,
        "value": "Delete Banner Photo"
      }
    ],
    "BusinessApplication.ApplicationBannerImageDesc": [
      {
        "type": 0,
        "value": "This will appear very large at the top of your profile page and must be landscape in ratio. It should show a completed project that's representative of your design style."
      }
    ],
    "BusinessApplication.ApplicationBannerImageTitle": [
      {
        "type": 0,
        "value": "Banner Image"
      }
    ],
    "BusinessApplication.ApplicationBannerUploadImageLabel": [
      {
        "type": 0,
        "value": "Upload Banner Photo"
      }
    ],
    "BusinessApplication.ApplicationFormBusinessHeader": [
      {
        "type": 0,
        "value": "Describe Your Business"
      }
    ],
    "BusinessApplication.ApplicationFormErrorHeader": [
      {
        "type": 0,
        "value": "The following errors must be corrected:"
      }
    ],
    "BusinessApplication.ApplicationFormSaveAndExitLink": [
      {
        "type": 0,
        "value": "Save & Exit Application"
      }
    ],
    "BusinessApplication.ApplicationFormSaveAndExitText": [
      {
        "type": 0,
        "value": "If you want to continue later,"
      }
    ],
    "BusinessApplication.ApplicationFormSectionHeader": [
      {
        "type": 0,
        "value": "About Your Business"
      }
    ],
    "BusinessApplication.ApplicationFormSectionSubHeader": [
      {
        "type": 0,
        "value": "You can save and return by selecting the ‘Save and Exit Application’ link at the bottom of the page."
      }
    ],
    "BusinessApplication.ApplicationImagesInlineValidationError": [
      {
        "type": 0,
        "value": "Images must be at least 1200 x 1200 pixels and no larger than 30MB. Please try again or select a different file."
      }
    ],
    "BusinessApplication.ApplicationModalExitButton": [
      {
        "type": 0,
        "value": "Exit Without Saving"
      }
    ],
    "BusinessApplication.ApplicationModalSaveExitButton": [
      {
        "type": 0,
        "value": "Save and exit"
      }
    ],
    "BusinessApplication.ApplicationPageSectionHeader": [
      {
        "type": 0,
        "value": "Create Your Profile"
      }
    ],
    "BusinessApplication.ApplicationPageSectionHeader2": [
      {
        "type": 0,
        "value": "Your Profile Application"
      }
    ],
    "BusinessApplication.ApplicationPageSectionSubHeader": [
      {
        "type": 0,
        "value": "Start your application by completing a business profile."
      }
    ],
    "BusinessApplication.ApplicationPhotoLabel": [
      {
        "type": 0,
        "value": "Photos"
      }
    ],
    "BusinessApplication.ApplicationPhotosDescription": [
      {
        "type": 0,
        "value": "Images must be JPEG or PNG format. Minimum size: 1200 x 1200 pixels. Maximum file size: 30MB."
      }
    ],
    "BusinessApplication.ApplicationPortfolioDeletePhotoLabel ": [
      {
        "type": 0,
        "value": "Delete Portfolio Photo"
      }
    ],
    "BusinessApplication.ApplicationProfileDeletePhotoLabel": [
      {
        "type": 0,
        "value": "Delete Profile Photo"
      }
    ],
    "BusinessApplication.ApplicationProfileImageDesc": [
      {
        "type": 0,
        "value": "This will appear next to your company name and contact details. You must upload an image that is square in ratio but it will automatically crop as you see in the preview. The photo can be of you, your colleagues or company logo."
      }
    ],
    "BusinessApplication.ApplicationProfileImageTitle": [
      {
        "type": 0,
        "value": "Profile Image"
      }
    ],
    "BusinessApplication.ApplicationProfileUploadImageLabel": [
      {
        "type": 0,
        "value": "Upload Profile Photo"
      }
    ],
    "BusinessApplication.ApplicationUploadImageLabel ": [
      {
        "type": 0,
        "value": "Upload Portfolio Photo &nbsp"
      }
    ],
    "BusinessApplication.ApplicationWorkImageDesc": [
      {
        "type": 0,
        "value": "The first will appear on the search results page. These should be of recent projects or work you have done. Include at least "
      },
      {
        "type": 1,
        "value": "minWorkImages"
      },
      {
        "type": 0,
        "value": "."
      }
    ],
    "BusinessApplication.ApplicationWorkImageTitle": [
      {
        "type": 0,
        "value": "Portfolio"
      }
    ],
    "BusinessApplication.ApprovedAccountProfileBtnLabel": [
      {
        "type": 0,
        "value": "Check My Profile"
      }
    ],
    "BusinessApplication.ApprovedAccountProfileDek": [
      {
        "type": 0,
        "value": "You're almost there! The AD PRO editors may have made minor changes to your page for consistency and style. To proceed, use the secure payment link in the email we sent you. If you have any questions, you can reach us at "
      },
      {
        "type": 1,
        "value": "email"
      },
      {
        "type": 0,
        "value": "."
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "Once payment is processed, you'll have access to all the AD PRO features, then receive a link to your profile once it's published ahead of launch."
      }
    ],
    "BusinessApplication.ApprovedAccountProfileHed": [
      {
        "type": 0,
        "value": "Your AD PRO Directory Application Has Been Approved"
      }
    ],
    "BusinessApplication.ApprovedBannerDek": [
      {
        "type": 0,
        "value": "Your profile is ready to be published. You cannot make any changes to it at this time."
      }
    ],
    "BusinessApplication.ApprovedBannerTitle": [
      {
        "type": 0,
        "value": "Application Approved"
      }
    ],
    "BusinessApplication.BannerIsResubmittedText": [
      {
        "type": 0,
        "value": "updated"
      }
    ],
    "BusinessApplication.BannerIsSubmittedText": [
      {
        "type": 0,
        "value": "submitted"
      }
    ],
    "BusinessApplication.BannerOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Upload a banner photo with the correct file type and size"
      }
    ],
    "BusinessApplication.CompanyBusinessTypeLabel": [
      {
        "type": 0,
        "value": "Choose a Category"
      }
    ],
    "BusinessApplication.CompanyBusinessTypeOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Choose a Business Category"
      }
    ],
    "BusinessApplication.CompanyCityInlineValidationError": [
      {
        "type": 0,
        "value": "Don't use special characters."
      }
    ],
    "BusinessApplication.CompanyCityLabel": [
      {
        "type": 0,
        "value": "CITY"
      }
    ],
    "BusinessApplication.CompanyCityOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Enter a City"
      }
    ],
    "BusinessApplication.CompanyCountryAssistiveLabel": [
      {
        "type": 0,
        "value": "This information will appear publicly on your profile."
      }
    ],
    "BusinessApplication.CompanyCountryLabel": [
      {
        "type": 0,
        "value": "COUNTRY"
      }
    ],
    "BusinessApplication.CompanyCountryRegisterHereLabel": [
      {
        "type": 0,
        "value": "register here"
      }
    ],
    "BusinessApplication.CompanyDescriptionLabel": [
      {
        "type": 0,
        "value": "YOUR BUSINESS IN DETAIL"
      }
    ],
    "BusinessApplication.CompanyDescriptionOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Enter the Business in Detail information. It must be between 1000 and 2000 characters."
      }
    ],
    "BusinessApplication.CompanyDescriptionPlaceholderText": [
      {
        "type": 0,
        "value": "Tell us about you and your business in more detail. What sets you apart from the competition? Do you specialize in a particular style? How do you prefer to work? What are some examples of recent projects? Please also note in this section if you are willing to travel for a job. This information will appear on your business profile page."
      }
    ],
    "BusinessApplication.CompanyEmailInlineValidationError": [
      {
        "type": 0,
        "value": "Check the email address is valid"
      }
    ],
    "BusinessApplication.CompanyEmailLabel": [
      {
        "type": 0,
        "value": "EMAIL ADDRESS"
      }
    ],
    "BusinessApplication.CompanyEmailOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Enter a valid Email Address"
      }
    ],
    "BusinessApplication.CompanyNameInlineValidationError": [
      {
        "type": 0,
        "value": "Use a maximum of 128 characters with no special characters"
      }
    ],
    "BusinessApplication.CompanyNameLabel": [
      {
        "type": 0,
        "value": "COMPANY NAME"
      }
    ],
    "BusinessApplication.CompanyNameOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Enter a Company Name with a maximum of 128 characters"
      }
    ],
    "BusinessApplication.CompanyPhoneInlineValidationError": [
      {
        "type": 0,
        "value": "Check the phone number is valid"
      }
    ],
    "BusinessApplication.CompanyPhoneLabel": [
      {
        "type": 0,
        "value": "PHONE NUMBER"
      }
    ],
    "BusinessApplication.CompanyPhoneOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Enter a valid Phone Number using only 10 digits"
      }
    ],
    "BusinessApplication.CompanyPhonePlaceholderText": [
      {
        "type": 0,
        "value": "Enter 10 digits only"
      }
    ],
    "BusinessApplication.CompanyProfessionLabel": [
      {
        "type": 0,
        "value": "Choose a Profession"
      }
    ],
    "BusinessApplication.CompanyProfessionOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Choose a Profession"
      }
    ],
    "BusinessApplication.CompanySocialUrlInlineValidationError": [
      {
        "type": 0,
        "value": "Don't use spaces"
      }
    ],
    "BusinessApplication.CompanySocialUrlLabel": [
      {
        "type": 0,
        "value": "Instagram username"
      }
    ],
    "BusinessApplication.CompanyStateLabel": [
      {
        "type": 0,
        "value": "STATE"
      }
    ],
    "BusinessApplication.CompanyStateOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Select a State"
      }
    ],
    "BusinessApplication.CompanyStatePlaceholderText": [
      {
        "type": 0,
        "value": "Select an option"
      }
    ],
    "BusinessApplication.CompanyStreetAddressLabel": [
      {
        "type": 0,
        "value": "STREET ADDRESS"
      }
    ],
    "BusinessApplication.CompanyStreetAddressOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Enter a Street Address"
      }
    ],
    "BusinessApplication.CompanyTagLineOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Enter the Business in Brief information. It must be between 80 and 120 characters."
      }
    ],
    "BusinessApplication.CompanyTaglineLabel": [
      {
        "type": 0,
        "value": "YOUR BUSINESS IN BRIEF"
      }
    ],
    "BusinessApplication.CompanyTaglinePlaceholderText": [
      {
        "type": 0,
        "value": "Tell us about you and your business and what makes you stand out from the competition. This will appear on the search results page when our readers look for someone in your profession so this should make them want to find out more."
      }
    ],
    "BusinessApplication.CompanyWebsiteInlineValidationError": [
      {
        "type": 0,
        "value": "Invalid URL format. Please include the https:// prefix, e.g., https://www.example.com."
      }
    ],
    "BusinessApplication.CompanyWebsiteLabel": [
      {
        "type": 0,
        "value": "WEBSITE"
      }
    ],
    "BusinessApplication.CompanyWebsitePlaceholderText": [
      {
        "type": 0,
        "value": "Optional"
      }
    ],
    "BusinessApplication.CompanyZipCodeInlineValidationError": [
      {
        "type": 0,
        "value": "Check the Zip Code is valid"
      }
    ],
    "BusinessApplication.CompanyZipCodeLabel": [
      {
        "type": 0,
        "value": "ZIP CODE"
      }
    ],
    "BusinessApplication.CompanyZipCodeOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Enter a valid ZIP Code"
      }
    ],
    "BusinessApplication.DataConsentLabel": [
      {
        "type": 0,
        "value": "I have read and accept the User Terms ("
      },
      {
        "type": 1,
        "value": "link"
      },
      {
        "type": 0,
        "value": ") and confirm that the content and images submitted as part of my application belong to me and do not and will not infringe, misappropriate or otherwise violate any third party rights, including without limitation, music, talent, logos, trademarks, copyright, or any other third party intellectual property rights. I understand and agree that Conde Nast will process my personal data in accordance with its Privacy Policy ("
      },
      {
        "type": 1,
        "value": "linkPrivacy"
      },
      {
        "type": 0,
        "value": ")"
      }
    ],
    "BusinessApplication.DefaultAccountProfileBtnLabel": [
      {
        "type": 0,
        "value": "Find Out More"
      }
    ],
    "BusinessApplication.DefaultAccountProfileDek": [
      {
        "type": 0,
        "value": "Create a personalized designer profile and list your business on our go-to guide for homeowners and renovators."
      }
    ],
    "BusinessApplication.DefaultAccountProfileHed": [
      {
        "type": 0,
        "value": "Introducing the AD PRO Directory"
      }
    ],
    "BusinessApplication.DraftAccountProfileBtnLabel": [
      {
        "type": 0,
        "value": "Go to My Application"
      }
    ],
    "BusinessApplication.DraftAccountProfileDek": [
      {
        "type": 0,
        "value": "You started a business profile on "
      },
      {
        "type": 1,
        "value": "submissionDate"
      },
      {
        "type": 0,
        "value": "."
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "Complete now and apply to join the industry's most respected roster of design talent."
      }
    ],
    "BusinessApplication.DraftAccountProfileHed": [
      {
        "type": 0,
        "value": "Your AD PRO Directory Application"
      }
    ],
    "BusinessApplication.DraftBannerDek": [
      {
        "type": 0,
        "value": "If you have any questions about your application or the AD PRO Directory, visit our "
      },
      {
        "type": 1,
        "value": "faq"
      },
      {
        "type": 0,
        "value": " or contact us at "
      },
      {
        "type": 1,
        "value": "email"
      },
      {
        "type": 0,
        "value": "."
      }
    ],
    "BusinessApplication.DraftBannerTitle": [
      {
        "type": 0,
        "value": "Your profile is incomplete"
      }
    ],
    "BusinessApplication.EditConsentLabel": [
      {
        "type": 0,
        "value": "You understand and agree that if your application is successful the "
      },
      {
        "type": 1,
        "value": "italicAD"
      },
      {
        "type": 0,
        "value": " editorial team will have editorial discretion in writing your AD PRO Directory profile using the information provided in your application. The "
      },
      {
        "type": 1,
        "value": "italicAD"
      },
      {
        "type": 0,
        "value": " editorial team cannot accommodate suggestions or changes to profiles once published other than in the case of correcting a factual inaccuracy."
      }
    ],
    "BusinessApplication.ExpiredAccountProfileBtnLabel": [
      {
        "type": 0,
        "value": "Restart"
      }
    ],
    "BusinessApplication.ExpiredAccountProfileDek": [
      {
        "type": 0,
        "value": "Restart your membership, by paying now."
      }
    ],
    "BusinessApplication.ExpiredAccountProfileHed": [
      {
        "type": 0,
        "value": "Your AD PRO Directory membership is no longer active."
      }
    ],
    "BusinessApplication.FormLabel": [
      {
        "type": 0,
        "value": "About Your Business"
      }
    ],
    "BusinessApplication.FormSubmitButtonLabel": [
      {
        "type": 0,
        "value": "SUBMIT APPLICATION"
      }
    ],
    "BusinessApplication.MessageBannerCtaButtonLabel": [
      {
        "type": 0,
        "value": "GO TO MY LISTING"
      }
    ],
    "BusinessApplication.NeedInputAccountProfileBtnLabel": [
      {
        "type": 0,
        "value": "Update My Application"
      }
    ],
    "BusinessApplication.NeedInputAccountProfileDek": [
      {
        "type": 0,
        "value": "The business profile you submitted on "
      },
      {
        "type": 1,
        "value": "submissionDate"
      },
      {
        "type": 0,
        "value": " has been reviewed."
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "A few changes are needed before we approve your listing. Please review the application form for our editors' comments and recommended next steps."
      }
    ],
    "BusinessApplication.NeedInputsBannerDek": [
      {
        "type": 0,
        "value": "After review, the AD PRO editors have the following comments:"
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 1,
        "value": "remark"
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "You can then resubmit your application for further review. If you have any questions about your application or the AD PRO Directory, visit our "
      },
      {
        "type": 1,
        "value": "faq"
      },
      {
        "type": 0,
        "value": " or contact us at "
      },
      {
        "type": 1,
        "value": "email"
      },
      {
        "type": 0,
        "value": "."
      }
    ],
    "BusinessApplication.NeedInputsBannerTitle": [
      {
        "type": 0,
        "value": "Our Feedback to You"
      }
    ],
    "BusinessApplication.PaymentDoneAccountProfileBtnLabel": [
      {
        "type": 0,
        "value": "Go to My Business Profile"
      }
    ],
    "BusinessApplication.PaymentDoneAccountProfileDek": [
      {
        "type": 0,
        "value": "Congratulations! We are pleased to welcome you to the AD PRO Directory."
      }
    ],
    "BusinessApplication.PaymentDoneAccountProfileHed": [
      {
        "type": 0,
        "value": "Your Profile is Live on the AD PRO Directory."
      }
    ],
    "BusinessApplication.PaymentDoneBannerDek": [
      {
        "type": 0,
        "value": "If you need to make changes to your listing, please email "
      },
      {
        "type": 1,
        "value": "email"
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 1,
        "value": "profileURL"
      }
    ],
    "BusinessApplication.PaymentDoneBannerTitle": [
      {
        "type": 0,
        "value": "Your profile is live on the AD PRO Directory"
      }
    ],
    "BusinessApplication.ProfileOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Upload a profile photo with the correct file type and size"
      }
    ],
    "BusinessApplication.RejectedAccountProfileDek": [
      {
        "type": 0,
        "value": "Thank you for your interest in joining the AD PRO Directory."
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "Unfortunately, we will not be able to accept your business at this time. We recognize this may be disappointing news, but you are welcome to apply again in the future. Please email our Directory team at "
      },
      {
        "type": 1,
        "value": "email"
      },
      {
        "type": 0,
        "value": " if you would like to reopen this application"
      }
    ],
    "BusinessApplication.RejectedBannerDek": [
      {
        "type": 0,
        "value": "You submitted this application on "
      },
      {
        "type": 1,
        "value": "submittedAt"
      },
      {
        "type": 0,
        "value": ". To reapply, please contact us at "
      },
      {
        "type": 1,
        "value": "email"
      },
      {
        "type": 0,
        "value": "."
      }
    ],
    "BusinessApplication.SubmitAccountProfileDek": [
      {
        "type": 0,
        "value": "The "
      },
      {
        "type": 1,
        "value": "italicAD"
      },
      {
        "type": 0,
        "value": " Editors are reviewing your business profile and will email you shortly."
      }
    ],
    "BusinessApplication.SubmitAccountProfileHed": [
      {
        "type": 0,
        "value": "We’ve Got Your "
      },
      {
        "type": 1,
        "value": "isResubmitted"
      },
      {
        "type": 0,
        "value": " AD PRO Directory Application"
      }
    ],
    "BusinessApplication.SubmitBannerDek": [
      {
        "type": 0,
        "value": "Application "
      },
      {
        "type": 1,
        "value": "isResubmitted"
      },
      {
        "type": 0,
        "value": " on "
      },
      {
        "type": 1,
        "value": "submittedAt"
      },
      {
        "type": 0,
        "value": ". "
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "Your business profile is being reviewed and you can't make any changes to it at this time. The Directory team will email you shortly."
      }
    ],
    "BusinessApplication.UnderReviewAccountProfileHed": [
      {
        "type": 0,
        "value": "We’ve Got Your Updated AD PRO Directory Application"
      }
    ],
    "BusinessApplication.UnderReviewBannerDek": [
      {
        "type": 0,
        "value": "Application updated on "
      },
      {
        "type": 1,
        "value": "submittedAt"
      },
      {
        "type": 0,
        "value": ". "
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "Your business profile is being reviewed and you can't make any changes to it at this time. The Directory team will email you shortly."
      }
    ],
    "BusinessApplication.WorkImageOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Upload at least 3 photos of your work with the correct file type and size"
      }
    ],
    "BusinessApplication.applicationModalButtonText": [
      {
        "type": 0,
        "value": "Continue with the Application"
      }
    ],
    "BusinessApplication.applicationModalMessage1": [
      {
        "type": 0,
        "value": "Ensure you have saved your application before leaving."
      }
    ],
    "BusinessApplication.applicationModalMessage2": [
      {
        "type": 0,
        "value": "Go to your AD account to complete your AD PRO Directory application"
      }
    ],
    "BusinessApplication.applicationPhotosAddInfoText": [
      {
        "type": 0,
        "value": "Add Info"
      }
    ],
    "BusinessApplication.applicationPhotosEditInfoText": [
      {
        "type": 0,
        "value": "Edit Info"
      }
    ],
    "BusinessApplication.applicationSessionErrorMessage": [
      {
        "type": 0,
        "value": "Something went wrong. Please try again."
      }
    ],
    "BusinessApplication.applicationWorkImageAdditionalDesc": [
      {
        "type": 0,
        "value": "Portfolio Photo 1 will appear on the search results page and must be landscape in ratio."
      }
    ],
    "BusinessApplication.captionPlaceholderText": [
      {
        "type": 0,
        "value": "Type your caption here. Captions are optional but should provide context to the user (e.g. location and scope of project)."
      }
    ],
    "BusinessApplication.creditPlaceholderText": [
      {
        "type": 0,
        "value": "Type your credit here. Credits are optional but please include the photographer’s name or image source if known."
      }
    ],
    "BusinessApplication.dataConsentOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Accept the user terms and conditions"
      }
    ],
    "BusinessApplication.editConsentOnSubmitValidationError": [
      {
        "type": 0,
        "value": "Please read and accept the terms"
      }
    ],
    "BusinessApplication.imageCaptionLabel": [
      {
        "type": 0,
        "value": "CAPTION"
      }
    ],
    "BusinessApplication.imageCreditCaptionUpdateLabel": [
      {
        "type": 0,
        "value": "UPDATE"
      }
    ],
    "BusinessApplication.imageCreditLabel": [
      {
        "type": 0,
        "value": "CREDIT"
      }
    ],
    "BusinessApplication.loginTimeoutModalSecondaryCTAButton": [
      {
        "type": 0,
        "value": "Go To Home Page"
      }
    ],
    "BusinessApplication.modalHeaderText": [
      {
        "type": 0,
        "value": "Photo caption and credit (optional)"
      }
    ],
    "BusinessApplication.timeoutModalHeaderText": [
      {
        "type": 0,
        "value": "This session will expire in"
      }
    ],
    "BusinessApplication.timeoutModalLoginSecondaryText": [
      {
        "type": 0,
        "value": "Please log in to your Account to continue with your application."
      }
    ],
    "BusinessApplication.timeoutModalPrimaryCTALoginButton": [
      {
        "type": 0,
        "value": "Login"
      }
    ],
    "BusinessApplication.timeoutModalSecondaryCTAButton": [
      {
        "type": 0,
        "value": "Save and Exit Application"
      }
    ],
    "BusinessApplication.timeoutModalSecondaryText": [
      {
        "type": 0,
        "value": "You will lose any unsaved changes."
      }
    ],
    "BusinessApplication.timeoutModalSessionExipreHeaderText": [
      {
        "type": 0,
        "value": "The session has expired."
      }
    ],
    "BusinessProfile.EditorialTitleHed": [
      {
        "type": 0,
        "value": "Editors' Take"
      }
    ],
    "BusinessProfile.ExploreTitleHed": [
      {
        "type": 0,
        "value": "More from AD"
      }
    ],
    "BusinessProfile.SectionTitleHed": [
      {
        "type": 0,
        "value": "About"
      }
    ],
    "BusinessProfile.businessProfileImageCreditPrefix": [
      {
        "type": 0,
        "value": "Photo by"
      }
    ],
    "Byline.More": [
      {
        "type": 0,
        "value": "more"
      }
    ],
    "Byline.Preamble": [
      {
        "type": 0,
        "value": "By"
      }
    ],
    "Bylines.AdaptationEditorPreamble": [
      {
        "type": 0,
        "value": "Translated and Adapted by"
      }
    ],
    "Bylines.AnimatorPreamble": [
      {
        "type": 0,
        "value": "Animation by"
      }
    ],
    "Bylines.ArtistPreamble": [
      {
        "type": 0,
        "value": "Art by"
      }
    ],
    "Bylines.ArtworkPreamble": [
      {
        "type": 0,
        "value": "Artwork by"
      }
    ],
    "Bylines.AstoldtoPreamble": [
      {
        "type": 0,
        "value": "As told to"
      }
    ],
    "Bylines.AuthorPreamble": [
      {
        "type": 0,
        "value": "By"
      }
    ],
    "Bylines.CoverShootPreamble": [
      {
        "type": 0,
        "value": "Cover Shoot by"
      }
    ],
    "Bylines.DeveloperPreamble": [
      {
        "type": 0,
        "value": "Development by"
      }
    ],
    "Bylines.DirectorPreamble": [
      {
        "type": 0,
        "value": "Directed by"
      }
    ],
    "Bylines.EditorPreamble": [
      {
        "type": 0,
        "value": "Edited by"
      }
    ],
    "Bylines.FilmByPreamble": [
      {
        "type": 0,
        "value": "Film by"
      }
    ],
    "Bylines.HairPreamble": [
      {
        "type": 0,
        "value": "Hair by"
      }
    ],
    "Bylines.IllustratorPreamble": [
      {
        "type": 0,
        "value": "Illustration by"
      }
    ],
    "Bylines.IntroducerPreamble": [
      {
        "type": 0,
        "value": "Introduced by"
      }
    ],
    "Bylines.MakeupPreamble": [
      {
        "type": 0,
        "value": "Makeup by"
      }
    ],
    "Bylines.MedicalReviewerPreamble": [
      {
        "type": 0,
        "value": "Medically reviewed by"
      }
    ],
    "Bylines.NailsPreamble": [
      {
        "type": 0,
        "value": "Nails by"
      }
    ],
    "Bylines.PhotographerPreamble": [
      {
        "type": 0,
        "value": "Photography by"
      }
    ],
    "Bylines.PodcasthostPreamble": [
      {
        "type": 0,
        "value": "With"
      }
    ],
    "Bylines.ProducerPreamble": [
      {
        "type": 0,
        "value": "Produced by"
      }
    ],
    "Bylines.ReporterPreamble": [
      {
        "type": 0,
        "value": "Reporting by"
      }
    ],
    "Bylines.ReviewerPreamble": [
      {
        "type": 0,
        "value": "Reviewed by"
      }
    ],
    "Bylines.StylistPreamble": [
      {
        "type": 0,
        "value": "Styled by"
      }
    ],
    "Bylines.TextByPreamble": [
      {
        "type": 0,
        "value": "Text by"
      }
    ],
    "Bylines.ToldbyPreamble": [
      {
        "type": 0,
        "value": "As told by"
      }
    ],
    "Bylines.VideoByPreamble": [
      {
        "type": 0,
        "value": "Video by"
      }
    ],
    "Bylines.VideoDirectorPreamble": [
      {
        "type": 0,
        "value": "Video Directed by"
      }
    ],
    "Bylines.WithPreamble": [
      {
        "type": 0,
        "value": "With"
      }
    ],
    "Bylines.Writer": [
      {
        "type": 0,
        "value": "Written by"
      }
    ],
    "Bylines.additionalReportingPreamble": [
      {
        "type": 0,
        "value": "Additional Reporting by"
      }
    ],
    "Bylines.inconversationPreamble": [
      {
        "type": 0,
        "value": "In Conversation with"
      }
    ],
    "Bylines.introductionPreamble": [
      {
        "type": 0,
        "value": "Introduction by"
      }
    ],
    "CNEVideoWatchPage.AboutPremiereDate": [
      {
        "type": 0,
        "value": "Released on "
      },
      {
        "type": 1,
        "value": "premiereDate"
      }
    ],
    "CNEVideoWatchPage.AboutPremiereDateFormat": [
      {
        "type": 0,
        "value": "MM/DD/YYYY"
      }
    ],
    "CNEVideoWatchPage.AboutTabLabel": [
      {
        "type": 0,
        "value": "About"
      }
    ],
    "CNEVideoWatchPage.CreditsTabLabel": [
      {
        "type": 0,
        "value": "Credits"
      }
    ],
    "CNEVideoWatchPage.PlaylistHeading": [
      {
        "type": 0,
        "value": "Up Next"
      }
    ],
    "CNEVideoWatchPage.PreviewHeading": [
      {
        "type": 0,
        "value": "Preview"
      }
    ],
    "CNEVideoWatchPage.PreviewLinkCopied": [
      {
        "type": 0,
        "value": "copied to clipboard"
      }
    ],
    "CNEVideoWatchPage.RubricEpisode": [
      {
        "type": 0,
        "value": "Episode "
      },
      {
        "type": 1,
        "value": "episode"
      }
    ],
    "CNEVideoWatchPage.TheaterModeLabel": [
      {
        "type": 0,
        "value": "Hide"
      }
    ],
    "CNEVideoWatchPage.TranscriptHeading": [
      {
        "type": 0,
        "value": "Transcript"
      }
    ],
    "CNEVideoWatchPage.TrendingRecsHeading": [
      {
        "type": 0,
        "value": "Trending video"
      }
    ],
    "CaptionContest.CaptionButton.authenticateSubmitButtonLabel": [
      {
        "type": 0,
        "value": "Sign in to submit"
      }
    ],
    "CaptionContest.CaptionButton.authenticateVoteButtonLabel": [
      {
        "type": 0,
        "value": "Sign in to vote"
      }
    ],
    "CaptionContest.CaptionButton.voteButtonLabel": [
      {
        "type": 0,
        "value": "Vote"
      }
    ],
    "CaptionContest.contestTabLoggedInDisclaimer": [
      {
        "type": 0,
        "value": "You must be thirteen or older to enter the contest. Your entry must be received by 11:59 P.M. E.T. on "
      },
      {
        "type": 1,
        "value": "submissionDeadline"
      },
      {
        "type": 0,
        "value": ", and must follow the "
      },
      {
        "children": [
          {
            "type": 0,
            "value": "official caption contest rules"
          }
        ],
        "type": 8,
        "value": "a"
      },
      {
        "type": 0,
        "value": "."
      },
      {
        "children": [],
        "type": 8,
        "value": "b"
      },
      {
        "type": 0,
        "value": "You can "
      },
      {
        "children": [
          {
            "type": 0,
            "value": "update your contact information"
          }
        ],
        "type": 8,
        "value": "c"
      },
      {
        "type": 0,
        "value": " anytime."
      }
    ],
    "CaptionContest.contestTabLoggedOutDisclaimer": [
      {
        "type": 0,
        "value": "You must be thirteen or older to enter the contest. Your entry must be received by 11:59 P.M. E.T. on "
      },
      {
        "type": 1,
        "value": "submissionDeadline"
      },
      {
        "type": 0,
        "value": ", and must follow the "
      },
      {
        "children": [
          {
            "type": 0,
            "value": "official caption contest rules"
          }
        ],
        "type": 8,
        "value": "a"
      },
      {
        "type": 0,
        "value": "."
      }
    ],
    "CaptionContest.fetchErrorMessage": [
      {
        "type": 0,
        "value": "There was a problem submitting your caption. Please try again later."
      }
    ],
    "CaptionContest.rateApiErrorMessage": [
      {
        "type": 0,
        "value": "Captions aren’t available right now. Come back later to rate them."
      }
    ],
    "CaptionContest.rateAuthButtonLabel": [
      {
        "type": 0,
        "value": "Sign in to rate captions"
      }
    ],
    "CaptionContest.rateButtonFunnyLabel": [
      {
        "type": 0,
        "value": "Funny"
      }
    ],
    "CaptionContest.rateButtonSomeWhatFunnyLabel": [
      {
        "type": 0,
        "value": "Somewhat funny"
      }
    ],
    "CaptionContest.rateCaptionsCompletedMessage": [
      {
        "type": 0,
        "value": "You've rated all of this week's captions!"
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "Please go do something (anything) else till next week."
      }
    ],
    "CaptionContest.rateLegacyButtonText": [
      {
        "type": 0,
        "value": "Start rating submissions"
      }
    ],
    "CaptionContest.rateLoadingText": [
      {
        "type": 0,
        "value": "Loading"
      }
    ],
    "CaptionContest.rateRecirculationDek": [
      {
        "type": 0,
        "value": "Rate submissions »"
      }
    ],
    "CaptionContest.rateRecirculationHed": [
      {
        "type": 0,
        "value": "Help us pick three finalists"
      }
    ],
    "CaptionContest.rateTabDisclaimer": [
      {
        "type": 0,
        "value": "All captions submitted by readers of "
      },
      {
        "children": [
          {
            "type": 0,
            "value": "brand"
          }
        ],
        "type": 8,
        "value": "i"
      },
      {
        "type": 0,
        "value": "."
      }
    ],
    "CaptionContest.recirculationHed": [
      {
        "type": 0,
        "value": "Next"
      }
    ],
    "CaptionContest.secondPlaceTitle": [
      {
        "type": 0,
        "value": "Second Place"
      }
    ],
    "CaptionContest.submitButtonLabel": [
      {
        "type": 0,
        "value": "Submit"
      }
    ],
    "CaptionContest.submitTabCounterErrorMsg": [
      {
        "type": 0,
        "value": "Use maximum of "
      },
      {
        "type": 1,
        "value": "maxCount"
      },
      {
        "type": 0,
        "value": " characters only."
      }
    ],
    "CaptionContest.submitTabUserInteractionLabel": [
      {
        "type": 0,
        "value": "Your Caption"
      }
    ],
    "CaptionContest.voteRecirculationDek": [
      {
        "type": 0,
        "value": "Vote on Finalists »"
      }
    ],
    "CaptionContest.voteRecirculationHed": [
      {
        "type": 0,
        "value": "Help choose the winner"
      }
    ],
    "CaptionContest.voteTabRecirculationHed": [
      {
        "type": 0,
        "value": "View results for "
      },
      {
        "type": 1,
        "value": "contestTitle"
      }
    ],
    "CaptionContest.winnerRecirculationDek": [
      {
        "type": 0,
        "value": "The Winner »"
      }
    ],
    "CaptionModal.captionModalButtonLabel": [
      {
        "type": 0,
        "value": "Save and submit caption"
      }
    ],
    "CaptionModal.captionModalDek": [
      {
        "type": 0,
        "value": "Add your name, location, and phone number, so we can contact and credit you if you're a finalist."
      }
    ],
    "CaptionModal.captionModalDisclaimerText": [
      {
        "children": [
          {
            "type": 0,
            "value": "Need help? Call: 1-800-444-7570 | E-mail: help@newyorker.com"
          }
        ],
        "type": 8,
        "value": "p"
      },
      {
        "children": [
          {
            "type": 0,
            "value": "We’re available Monday through Friday, 9 A.M. to 9 P.M. E.T., and Saturday through Sun, 9 A.M. to 5 P.M. E.T."
          }
        ],
        "type": 8,
        "value": "p"
      }
    ],
    "CaptionModal.captionModalHed": [
      {
        "type": 0,
        "value": "How would you like to be acknowledged?"
      }
    ],
    "CarouselControls.BackAriaLabel": [
      {
        "type": 0,
        "value": "Carousel back"
      }
    ],
    "CarouselControls.ForwardAriaLabel": [
      {
        "type": 0,
        "value": "Carousel forward"
      }
    ],
    "CartoonContest.contestCartoonCredit": [
      {
        "type": 0,
        "value": "Cartoon by "
      },
      {
        "type": 1,
        "value": "credit"
      }
    ],
    "CartoonContest.fetchErrorMessage": [
      {
        "type": 0,
        "value": "There was an issue submitting your vote. Please try again later."
      }
    ],
    "CartoonContest.instructionsButtonLabel": [
      {
        "type": 0,
        "value": "How does it work?"
      }
    ],
    "CartoonContest.rateButtonUnFunnyLabel": [
      {
        "type": 0,
        "value": "Unfunny"
      }
    ],
    "CartoonContest.rateTabDek": [
      {
        "type": 0,
        "value": "Your responses will help us select three finalists for "
      },
      {
        "type": 1,
        "value": "title"
      },
      {
        "type": 0,
        "value": "."
      }
    ],
    "CartoonContest.rateTabHed": [
      {
        "type": 0,
        "value": "Rate Submissions"
      }
    ],
    "CartoonContest.stageRate": [
      {
        "type": 0,
        "value": "Rate"
      }
    ],
    "CartoonContest.stageSubmit": [
      {
        "type": 0,
        "value": "Submit"
      }
    ],
    "CartoonContest.stageVote": [
      {
        "type": 0,
        "value": "Vote"
      }
    ],
    "CartoonContest.stageWinner": [
      {
        "type": 0,
        "value": "Winner"
      }
    ],
    "CartoonContest.submitSuccessMessage": [
      {
        "type": 0,
        "value": "Thanks for your submission. Check back on "
      },
      {
        "type": 1,
        "value": "finalistDate"
      },
      {
        "type": 0,
        "value": " to see the finalists. If your caption is among them, we’ll be in touch."
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "While you wait, you can rate reader-submitted captions from last week’s contest."
      }
    ],
    "CartoonContest.submitTabDek": [
      {
        "type": 0,
        "value": "Your caption for "
      },
      {
        "type": 1,
        "value": "title"
      },
      {
        "type": 0,
        "value": " will be rated by readers, like you, in the next round."
      }
    ],
    "CartoonContest.submitTabHed": [
      {
        "type": 0,
        "value": "Submit Your Caption"
      }
    ],
    "CartoonContest.thirdPlaceTitle": [
      {
        "type": 0,
        "value": "Third Place"
      }
    ],
    "CartoonContest.voteSuccessMessage": [
      {
        "type": 0,
        "value": "Thanks for your vote."
      },
      {
        "type": 0,
        "value": "<br/>"
      },
      {
        "type": 0,
        "value": "The next set of finalists’ captions will appear on "
      },
      {
        "type": 1,
        "value": "finalistDate"
      },
      {
        "type": 0,
        "value": "."
      }
    ],
    "CartoonContest.voteTabDek": [
      {
        "type": 0,
        "value": "Your choice will help determine the winning caption for "
      },
      {
        "type": 1,
        "value": "title"
      },
      {
        "type": 0,
        "value": "."
      }
    ],
    "CartoonContest.voteTabHed": [
      {
        "type": 0,
        "value": "Vote on Finalists"
      }
    ],
    "CartoonContest.winnerTabDek": [
      {
        "type": 1,
        "value": "title"
      }
    ],
    "CartoonContest.winnerTabHed": [
      {
        "type": 0,
        "value": "The Winner"
      }
    ],
    "Ceros.IframeTitle": [
      {
        "type": 0,
        "value": "Ceros embed"
      }
    ],
    "ChannelFilter.ClearAll": [
      {
        "type": 0,
        "value": "Clear All"
      }
    ],
    "ChannelFilter.ClearAllFiltersText": [
      {
        "type": 0,
        "value": "Clear All Filters and Keywords"
      }
    ],
    "ChannelFilter.FilterPreamble": [
      {
        "type": 0,
        "value": "Filter by"
      }
    ],
    "ChannelFilter.Save": [
      {
        "type": 0,
        "value": "Save"
      }
    ],
    "ChannelFilter.StoryCount": [
      {
        "type": 0,
        "value": "Showing "
      },
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Story"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Stories"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "storyCount"
      }
    ],
    "ChannelNavigation.ChannelDrawerContentLabel": [
      {
        "type": 0,
        "value": "Runway filters navigation"
      }
    ],
    "ChannelNavigation.GlobalDrawerContentLabel": [
      {
        "type": 0,
        "value": "Navigation Menu"
      }
    ],
    "ChannelNavigation.ToggleLabel": [
      {
        "type": 0,
        "value": "Open Navigation Menu"
      }
    ],
    "Clamp.ReadLess": [
      {
        "type": 0,
        "value": "Read less"
      }
    ],
    "Clamp.ReadMore": [
      {
        "type": 0,
        "value": "Read more"
      }
    ],
    "CneVideoEmbed.Live": [
      {
        "type": 0,
        "value": "• Live"
      }
    ],
    "CneVideoEmbed.PersistantCloseTitle": [
      {
        "type": 0,
        "value": "Close Persisted Player"
      }
    ],
    "CneVideoEmbed.WatchNow": [
      {
        "type": 0,
        "value": "Streaming Live Now"
      }
    ],
    "CollectionsDrawer.bookmarkCountType": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " image"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " images"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "count"
      }
    ],
    "CollectionsDrawer.bookmarkSavedText": [
      {
        "type": 0,
        "value": "Image saved"
      }
    ],
    "CollectionsDrawer.collectionsListHeading": [
      {
        "type": 0,
        "value": "Choose A Board"
      }
    ],
    "CollectionsDrawer.collectionsNewCollectionButtonLabel": [
      {
        "type": 0,
        "value": "New Board"
      }
    ],
    "CollectionsDrawer.createCollectionDuplicateNameError": [
      {
        "type": 0,
        "value": "You have already used this name"
      }
    ],
    "CollectionsDrawer.createCollectionNotMadeError": [
      {
        "type": 0,
        "value": "Collection not made, please try again"
      }
    ],
    "ComingSoon.SeriesNavigation": [
      {
        "type": 0,
        "value": "COMING SOON"
      }
    ],
    "Commenting.CommunityGuidelines": [
      {
        "type": 0,
        "value": "Community Guidelines"
      }
    ],
    "Commenting.LikeActionErrorMessage": [
      {
        "type": 0,
        "value": "Unable to like this comment. Please try again."
      }
    ],
    "Commenting.MessageBannerContentHed": [
      {
        "type": 0,
        "value": "Comments are moderated in line with our"
      }
    ],
    "Commenting.MessageBannerContentTrail": [
      {
        "type": 0,
        "value": "before being added."
      }
    ],
    "Commenting.MessageBannerSubContent": [
      {
        "type": 0,
        "value": "Thanks for contributing to this space."
      }
    ],
    "Commenting.MessageBannerTitle": [
      {
        "type": 0,
        "value": "Comment submitted"
      }
    ],
    "Commenting.UnlikeActionErrorMessage": [
      {
        "type": 0,
        "value": "Unable to unlike this comment. Please try again."
      }
    ],
    "Commenting.closeCommentStreamMessage": [
      {
        "type": 0,
        "value": "Comments are closed on this story but you can still browse or upvote them."
      }
    ],
    "Commenting.replyDiscardModalHed": [
      {
        "type": 0,
        "value": "Discard this reply?"
      }
    ],
    "Commenting.signInModalHed": [
      {
        "type": 0,
        "value": "Sign in to join the"
      }
    ],
    "Commenting.signInModalHedSpanTag": [
      {
        "type": 1,
        "value": "brandName"
      },
      {
        "type": 0,
        "value": " community"
      }
    ],
    "Commenting.signInModalMessage": [
      {
        "type": 0,
        "value": "Once you're signed in, add your comments and like or reply to others."
      }
    ],
    "ConnectedNewsletterSubscribeForm.BadResponse": [
      {
        "type": 0,
        "value": "Bad response for signup newsletter"
      }
    ],
    "ConnectedNewsletterSubscribeForm.ErrorMessage": [
      {
        "type": 0,
        "value": "Subscription failed:"
      }
    ],
    "ConnectedNewsletterSubscribeForm.SuccessDek": [
      {
        "type": 0,
        "value": "You've successfully subscribed to our newsletter...."
      }
    ],
    "ConnectedNewsletterSubscribeForm.SuccessHed": [
      {
        "type": 0,
        "value": "You're all set..."
      }
    ],
    "ConnectedNewsletterSubscribeForm.TypeMismatchMessage": [
      {
        "type": 0,
        "value": "Invalid email. Double check and try again."
      }
    ],
    "ConsentBanner.consentText": [
      {
        "type": 0,
        "value": "This content can also be viewed on the site it "
      },
      {
        "children": [
          {
            "type": 0,
            "value": "originates"
          }
        ],
        "type": 8,
        "value": "a"
      },
      {
        "type": 0,
        "value": " from."
      }
    ],
    "ConsentBanner.consentWarningText": [
      {
        "type": 0,
        "value": "To honor your privacy preferences, this content can only be viewed on the site it "
      },
      {
        "children": [
          {
            "type": 0,
            "value": "originates"
          }
        ],
        "type": 8,
        "value": "a"
      },
      {
        "type": 0,
        "value": " from."
      }
    ],
    "ContentCardEmbed.articleButtonCta": [
      {
        "type": 0,
        "value": "View Story"
      }
    ],
    "ContentCardEmbed.recipeButtonCta": [
      {
        "type": 0,
        "value": "View Recipe"
      }
    ],
    "ContentHeader.ReadReviews": [
      {
        "type": 0,
        "value": "Read Reviews"
      }
    ],
    "ContentHeader.ShowAllPhotos": [
      {
        "type": 0,
        "value": "Show all Photos"
      }
    ],
    "ContentPageControlRow.NextPage": [
      {
        "type": 0,
        "value": "Next"
      }
    ],
    "ContentPageControlRow.PreviousPage": [
      {
        "type": 0,
        "value": "Previous"
      }
    ],
    "ContentPageControlRow.ofHed": [
      {
        "type": 0,
        "value": "Of"
      }
    ],
    "ContentPromoEmbed.DefaultButtonText": [
      {
        "type": 0,
        "value": "Read More"
      }
    ],
    "ContentPromoEmbed.GalleryButtonText": [
      {
        "type": 0,
        "value": "View Slideshow"
      }
    ],
    "ContentsList.contentsListTitle": [
      {
        "type": 0,
        "value": "Table of Contents"
      }
    ],
    "ContributorHeader.SeeMoreContributorLink": [
      {
        "type": 0,
        "value": "See More By"
      }
    ],
    "ContributorPage.LoadMoreLoadingText": [
      {
        "type": 0,
        "value": "Loading ..."
      }
    ],
    "ContributorPage.LoadMoreText": [
      {
        "type": 0,
        "value": "More Stories"
      }
    ],
    "ContributorPage.featuredStoriesHedText": [
      {
        "type": 0,
        "value": "Featured Articles"
      }
    ],
    "ContributorPage.sectionHedText": [
      {
        "type": 0,
        "value": "Archive"
      }
    ],
    "Contributors.AuthorPreamble": [
      {
        "type": 0,
        "value": "Written by "
      },
      {
        "type": 1,
        "value": "brandName"
      },
      {
        "type": 0,
        "value": " Staff"
      }
    ],
    "CreateCollectionDrawer.createCollectionHeading": [
      {
        "type": 0,
        "value": "Create A Board"
      }
    ],
    "CreateCollectionDrawer.createCollectionInputLabel": [
      {
        "type": 0,
        "value": "Board Name"
      }
    ],
    "CreateCollectionDrawer.createCollectionNoTextError": [
      {
        "type": 0,
        "value": "Please enter some text"
      }
    ],
    "CreateCollectionDrawer.createCollectionPlaceholderText": [
      {
        "type": 0,
        "value": "Example: “monochrome” or “fall inspo”"
      }
    ],
    "CreateCollectionDrawer.createCollectionResetButtonLabel": [
      {
        "type": 0,
        "value": "Reset Board Name"
      }
    ],
    "CreateCollectionDrawer.createCollectionSubmitButtonLabel": [
      {
        "type": 0,
        "value": "Create"
      }
    ],
    "CreateCollectionDrawer.createCollectionValueMissingError": [
      {
        "type": 0,
        "value": "Please enter a collection name"
      }
    ],
    "CrosswordEmbed.SignInMessage": [
      {
        "type": 0,
        "value": "To save your progress, sign in to your "
      },
      {
        "children": [
          {
            "type": 1,
            "value": "portal"
          }
        ],
        "type": 8,
        "value": "emTag"
      },
      {
        "type": 0,
        "value": " account."
      }
    ],
    "CrosswordEmbed.Title": [
      {
        "type": 0,
        "value": "Embedded Crossword"
      }
    ],
    "CuratedShows.ButtonLabel": [
      {
        "type": 0,
        "value": "View all shows"
      }
    ],
    "CuratedShows.DrawerContentLabel": [
      {
        "type": 0,
        "value": "Runway All Shows navigation"
      }
    ],
    "CuratedShows.GroupedNavigationBrowserFilterLabel": [
      {
        "type": 0,
        "value": "Search..."
      }
    ],
    "CuratedShows.GroupedNavigationFilterLabel": [
      {
        "type": 0,
        "value": "Search for a designer..."
      }
    ],
    "CuratedShows.GroupedNavigationSummaryCarouselFilterLabel": [
      {
        "type": 0,
        "value": "Search..."
      }
    ],
    "CustomMenuButtons.Apply": [
      {
        "type": 0,
        "value": "APPLY"
      }
    ],
    "CustomMenuButtons.ClearAll": [
      {
        "type": 0,
        "value": "Clear all"
      }
    ],
    "Disclaimer.Text": [
      {
        "type": 0,
        "value": "All products featured on "
      },
      {
        "type": 1,
        "value": "brandName"
      },
      {
        "type": 0,
        "value": " are independently selected by our editors. However, when you buy something through our retail links, we may earn an affiliate commission."
      }
    ],
    "Drawer.ButtonLabel": [
      {
        "type": 0,
        "value": "Close drawer"
      }
    ],
    "Drawer.ContentLabel": [
      {
        "type": 0,
        "value": "Secondary menu navigation"
      }
    ],
    "DynamicChannelNav.PrimaryLinks": [
      {
        "type": 0,
        "value": "Primary"
      }
    ],
    "ErrorBoundary.ErrorMessage": [
      {
        "type": 0,
        "value": "An error occurred."
      }
    ],
    "ErrorContent.buttonLabel": [
      {
        "type": 0,
        "value": "Go to Homepage"
      }
    ],
    "ErrorContent.buttonLink": [
      {
        "type": 0,
        "value": "/"
      }
    ],
    "ErrorContent.dangerousDek": [
      {
        "type": 0,
        "value": "There was an issue with this page"
      }
    ],
    "ErrorContent.dangerousHed": [
      {
        "type": 0,
        "value": "Oops"
      }
    ],
    "ErrorPage.buttonLabel": [
      {
        "type": 0,
        "value": "Go to Homepage"
      }
    ],
    "ErrorPage.buttonLink": [
      {
        "type": 0,
        "value": "/"
      }
    ],
    "ErrorPage.dangerousDek": [
      {
        "type": 0,
        "value": "There was an issue with this page"
      }
    ],
    "ErrorPage.dangerousHed": [
      {
        "type": 0,
        "value": "Oops"
      }
    ],
    "ErrorPage.statusCodePreamble": [
      {
        "type": 0,
        "value": "Status Code"
      }
    ],
    "EventBanner.CloseBanner": [
      {
        "type": 0,
        "value": "Close Banner"
      }
    ],
    "EventBanner.LiveOn": [
      {
        "type": 0,
        "value": "Live on"
      }
    ],
    "EventBanner.SponsorPreamble": [
      {
        "type": 0,
        "value": "Countdown Presented By"
      }
    ],
    "EventBanner.WatchLiveOn": [
      {
        "type": 0,
        "value": "Watch live on"
      }
    ],
    "EventBanner.eventDays": [
      {
        "type": 0,
        "value": "Days"
      }
    ],
    "EventBanner.eventHours": [
      {
        "type": 0,
        "value": "Hours"
      }
    ],
    "EventBanner.eventMinutes": [
      {
        "type": 0,
        "value": "Minutes"
      }
    ],
    "EventBanner.eventSeconds": [
      {
        "type": 0,
        "value": "Seconds"
      }
    ],
    "EventsList.Title": [
      {
        "type": 0,
        "value": "Featured Events"
      }
    ],
    "ExternalLinkEmbed.Rubric": [
      {
        "type": 0,
        "value": "Read More"
      }
    ],
    "FacebookEmbed.AriaLabelText": [
      {
        "type": 0,
        "value": "social media post"
      }
    ],
    "FacebookEmbed.ConsentBannerHeader": [
      {
        "type": 0,
        "value": "Facebook content"
      }
    ],
    "FeaturedContributor.ViewMore": [
      {
        "type": 0,
        "value": "View more"
      }
    ],
    "FeaturedContributorAllFiction.ViewMore": [
      {
        "type": 0,
        "value": "View more"
      }
    ],
    "FeaturedStories.HedText": [
      {
        "type": 0,
        "value": "Featured Articles By "
      },
      {
        "type": 1,
        "value": "contributorName"
      }
    ],
    "Filmstrip.CollapsedMessage": [
      {
        "type": 0,
        "value": "Explore"
      }
    ],
    "Filmstrip.expandedMessage": [
      {
        "type": 0,
        "value": "Hide"
      }
    ],
    "Filter.FilterDropdownButton": [
      {
        "type": 0,
        "value": "Filter"
      }
    ],
    "Filter.ShowAllTags": [
      {
        "type": 0,
        "value": "SHOW ALL"
      }
    ],
    "Filter.ShowLessTags": [
      {
        "type": 0,
        "value": "SHOW LESS"
      }
    ],
    "FilterComponent.ContentLoadingLabel": [
      {
        "type": 0,
        "value": "Updating"
      }
    ],
    "FilterComponent.FilterApplyActionButton": [
      {
        "type": 0,
        "value": "Apply"
      }
    ],
    "FilterComponent.FilterBy": [
      {
        "type": 0,
        "value": "Filter by"
      }
    ],
    "FilterComponent.FilterCancelActionButton": [
      {
        "type": 0,
        "value": "Cancel"
      }
    ],
    "FilterComponent.FilterDeselectActionButton": [
      {
        "type": 0,
        "value": "Unselect all"
      }
    ],
    "FilterComponent.FilterMenuCloseButton": [
      {
        "type": 0,
        "value": "Close Filter Menu"
      }
    ],
    "FilterComponent.Items": [
      {
        "type": 0,
        "value": "Items"
      }
    ],
    "FilterComponent.NoResultDek": [
      {
        "type": 0,
        "value": "Sorry, we can't display any results for those filtering options, please try again."
      }
    ],
    "FilterComponent.NoResultHed": [
      {
        "type": 0,
        "value": "No Result"
      }
    ],
    "FilterComponent.ShowItems": [
      {
        "type": 0,
        "value": "Show "
      },
      {
        "type": 1,
        "value": "totalItems"
      },
      {
        "type": 0,
        "value": " Results"
      }
    ],
    "FilterComponent.SortBy": [
      {
        "type": 0,
        "value": "Sort by"
      }
    ],
    "FilterComponent.TotalCount": [
      {
        "type": 0,
        "value": "Results"
      }
    ],
    "FilterComponent.reviewTags": [
      {
        "type": 1,
        "value": "reviewTag"
      }
    ],
    "FilterableSummaryList.AtArticleGalleryCarouselBtnText": [
      {
        "type": 0,
        "value": "VIEW ALL "
      },
      {
        "type": 1,
        "value": "categoryName"
      }
    ],
    "FilterableSummaryList.AtArticleGalleryCarouselBtnTextWithCtaLink": [
      {
        "type": 1,
        "value": "categoryName"
      }
    ],
    "FireworkEmbed.ConsentBannerHeader": [
      {
        "type": 0,
        "value": "Firework content"
      }
    ],
    "FormWithValidation.BadInput": [
      {
        "type": 0,
        "value": "Bad input"
      }
    ],
    "FormWithValidation.CustomError": [
      {
        "type": 0,
        "value": "Custom error"
      }
    ],
    "FormWithValidation.InvalidValueMessage": [
      {
        "type": 1,
        "value": "field"
      },
      {
        "type": 0,
        "value": " is invalid."
      }
    ],
    "FormWithValidation.PatternMismatch": [
      {
        "type": 0,
        "value": "Pattern mismatch"
      }
    ],
    "FormWithValidation.RangeOverflow": [
      {
        "type": 0,
        "value": "Range overflow"
      }
    ],
    "FormWithValidation.RangeUnderflow": [
      {
        "type": 0,
        "value": "Range underflow"
      }
    ],
    "FormWithValidation.StepMismatch": [
      {
        "type": 0,
        "value": "Step mismatch"
      }
    ],
    "FormWithValidation.TooLong": [
      {
        "type": 0,
        "value": "Too long"
      }
    ],
    "FormWithValidation.TooShort": [
      {
        "type": 0,
        "value": "Too short"
      }
    ],
    "FormWithValidation.TypeMismatch": [
      {
        "type": 0,
        "value": "Type mismatch"
      }
    ],
    "FormWithValidation.ValueMissing": [
      {
        "type": 0,
        "value": "This field cannot be empty"
      }
    ],
    "GalleryCarousel.Next": [
      {
        "type": 0,
        "value": "Next"
      }
    ],
    "GalleryCarousel.NextGallery": [
      {
        "type": 0,
        "value": "Next gallery"
      }
    ],
    "GalleryCarousel.Previous": [
      {
        "type": 0,
        "value": "Previous"
      }
    ],
    "GalleryEmbedControls.AdSlideText": [
      {
        "type": 0,
        "value": "Advertisement"
      }
    ],
    "GalleryEmbedControls.BackArrowButtonAriaLabel": [
      {
        "type": 0,
        "value": "gallery-back"
      }
    ],
    "GalleryEmbedControls.ForwardArrowButtonAriaLabel": [
      {
        "type": 0,
        "value": "gallery-forward"
      }
    ],
    "GalleryPage.SignInCalloutLinkText": [
      {
        "type": 0,
        "value": "Sign in or create an account to vote"
      }
    ],
    "GalleryRecircCards.ViewGalleryCTAText": [
      {
        "type": 0,
        "value": "View gallery »"
      }
    ],
    "GalleryRecircCards.keepOnLaughingText": [
      {
        "type": 0,
        "value": "Keep on laughing"
      }
    ],
    "GalleryRecircCards.midGalleryRecircHeading": [
      {
        "type": 0,
        "value": "Want more laughs? Try another cartoon gallery."
      }
    ],
    "GalleryRecircCards.viewNextGalleryCTAText": [
      {
        "type": 0,
        "value": "View next gallery »"
      }
    ],
    "GallerySlide.ArticleCta": [
      {
        "type": 0,
        "value": "View Story"
      }
    ],
    "GallerySlide.DefaultCTAText": [
      {
        "type": 0,
        "value": "Book Now"
      }
    ],
    "GallerySlide.ProductCta": [
      {
        "type": 0,
        "value": "Shop Now"
      }
    ],
    "GallerySlide.RecipeCta": [
      {
        "type": 0,
        "value": "View Recipe"
      }
    ],
    "GallerySlide.ReviewCta": [
      {
        "type": 0,
        "value": "Read More"
      }
    ],
    "GallerySlide.VenueCta": [
      {
        "type": 0,
        "value": "Book Now"
      }
    ],
    "GallerySlide.VenueSellerPreviewText": [
      {
        "type": 0,
        "value": "Powered By:"
      }
    ],
    "GalleryVoting.galleryVotingDangerousDek": [
      {
        "type": 0,
        "value": "You can also save stories and manage newsletter preferences"
      }
    ],
    "GalleryVoting.galleryVotingDangerousHed": [
      {
        "type": 0,
        "value": "To vote, sign in or"
      }
    ],
    "GalleryVoting.galleryVotingDangerousHedSpanTag": [
      {
        "type": 0,
        "value": "create an account"
      }
    ],
    "GoogleSignInButton.Label": [
      {
        "type": 0,
        "value": "Sign in with Google"
      }
    ],
    "GroupedNavigation.FilterInputAriaLabel": [
      {
        "type": 0,
        "value": "Filter links"
      }
    ],
    "GroupedNavigationHasBrowser.FilterInputAriaLabel": [
      {
        "type": 0,
        "value": "Filter links"
      }
    ],
    "GroupedNavigationHasSummaryCarousel.FilterInputAriaLabel": [
      {
        "type": 0,
        "value": "Filter links"
      }
    ],
    "Icons.Account": [
      {
        "type": 0,
        "value": "Account"
      }
    ],
    "Icons.AgeGate": [
      {
        "type": 0,
        "value": "Age Gate"
      }
    ],
    "Icons.Arrow": [
      {
        "type": 0,
        "value": "Arrow"
      }
    ],
    "Icons.Article": [
      {
        "type": 0,
        "value": "Article"
      }
    ],
    "Icons.Bookmark": [
      {
        "type": 0,
        "value": "Save Story"
      }
    ],
    "Icons.BookmarkActivated": [
      {
        "type": 0,
        "value": "Story Saved"
      }
    ],
    "Icons.Cart": [
      {
        "type": 0,
        "value": "Cart"
      }
    ],
    "Icons.Check": [
      {
        "type": 0,
        "value": "Check"
      }
    ],
    "Icons.Chevron": [
      {
        "type": 0,
        "value": "Chevron"
      }
    ],
    "Icons.ChevronDown": [
      {
        "type": 0,
        "value": "Chevron Down"
      }
    ],
    "Icons.ChevronLeft": [
      {
        "type": 0,
        "value": "Chevron Left"
      }
    ],
    "Icons.ChevronUp": [
      {
        "type": 0,
        "value": "Chevron Up"
      }
    ],
    "Icons.Close": [
      {
        "type": 0,
        "value": "Close"
      }
    ],
    "Icons.Collapse": [
      {
        "type": 0,
        "value": "Collapse"
      }
    ],
    "Icons.Comment": [
      {
        "type": 0,
        "value": "Comment"
      }
    ],
    "Icons.CopyLink": [
      {
        "type": 0,
        "value": "CopyLink"
      }
    ],
    "Icons.Dots": [
      {
        "type": 0,
        "value": "Dots"
      }
    ],
    "Icons.DownloadCloud": [
      {
        "type": 0,
        "value": "DownloadCloud"
      }
    ],
    "Icons.DownloadWeb": [
      {
        "type": 0,
        "value": "DownloadWeb"
      }
    ],
    "Icons.Email": [
      {
        "type": 0,
        "value": "Email"
      }
    ],
    "Icons.Expand": [
      {
        "type": 0,
        "value": "Expand"
      }
    ],
    "Icons.Facebook": [
      {
        "type": 0,
        "value": "Facebook"
      }
    ],
    "Icons.Filmstrip": [
      {
        "type": 0,
        "value": "Filmstrip"
      }
    ],
    "Icons.Filter": [
      {
        "type": 0,
        "value": "Filter"
      }
    ],
    "Icons.Flipboard": [
      {
        "type": 0,
        "value": "Flipboard"
      }
    ],
    "Icons.Gallery": [
      {
        "type": 0,
        "value": "Gallery"
      }
    ],
    "Icons.GoogleNews": [
      {
        "type": 0,
        "value": "Google News"
      }
    ],
    "Icons.Grid": [
      {
        "type": 0,
        "value": "Grid"
      }
    ],
    "Icons.Headphone": [
      {
        "type": 0,
        "value": "Headphone"
      }
    ],
    "Icons.Information": [
      {
        "type": 0,
        "value": "Information"
      }
    ],
    "Icons.Instagram": [
      {
        "type": 0,
        "value": "Instagram"
      }
    ],
    "Icons.LargeChevron": [
      {
        "type": 0,
        "value": "LargeChevron"
      }
    ],
    "Icons.Like": [
      {
        "type": 0,
        "value": "Like"
      }
    ],
    "Icons.LikeFilled": [
      {
        "type": 0,
        "value": "LikeFilled"
      }
    ],
    "Icons.Line": [
      {
        "type": 0,
        "value": "Line"
      }
    ],
    "Icons.LinkedIn": [
      {
        "type": 0,
        "value": "LinkedIn"
      }
    ],
    "Icons.List": [
      {
        "type": 0,
        "value": "List"
      }
    ],
    "Icons.Loader": [
      {
        "type": 0,
        "value": "Loader"
      }
    ],
    "Icons.Maximize": [
      {
        "type": 0,
        "value": "Maximize"
      }
    ],
    "Icons.Menu": [
      {
        "type": 0,
        "value": "Menu"
      }
    ],
    "Icons.NativeShare": [
      {
        "type": 0,
        "value": "Native Share"
      }
    ],
    "Icons.Newsletter": [
      {
        "type": 0,
        "value": "Newsletter"
      }
    ],
    "Icons.Ok": [
      {
        "type": 0,
        "value": "Odnoklassniki"
      }
    ],
    "Icons.Passkey": [
      {
        "type": 0,
        "value": "Passkey"
      }
    ],
    "Icons.Pause": [
      {
        "type": 0,
        "value": "Pause"
      }
    ],
    "Icons.PhotoStack": [
      {
        "type": 0,
        "value": "PhotoStack"
      }
    ],
    "Icons.Pinterest": [
      {
        "type": 0,
        "value": "Pinterest"
      }
    ],
    "Icons.Play": [
      {
        "type": 0,
        "value": "Play"
      }
    ],
    "Icons.PlayCNE": [
      {
        "type": 0,
        "value": "PlayCNE"
      }
    ],
    "Icons.PlayOutlined": [
      {
        "type": 0,
        "value": "PlayOutlined"
      }
    ],
    "Icons.Playlist": [
      {
        "type": 0,
        "value": "Playlist"
      }
    ],
    "Icons.Print": [
      {
        "type": 0,
        "value": "Print"
      }
    ],
    "Icons.RatingFilled": [
      {
        "type": 0,
        "value": "RatingFilled"
      }
    ],
    "Icons.RatingHalf": [
      {
        "type": 0,
        "value": "RatingHalf"
      }
    ],
    "Icons.RatingOutlined": [
      {
        "type": 0,
        "value": "RatingOutlined"
      }
    ],
    "Icons.Replay": [
      {
        "type": 0,
        "value": "Replay"
      }
    ],
    "Icons.Rss": [
      {
        "type": 0,
        "value": "Rss"
      }
    ],
    "Icons.Search": [
      {
        "type": 0,
        "value": "Search"
      }
    ],
    "Icons.Share": [
      {
        "type": 0,
        "value": "Share"
      }
    ],
    "Icons.Shopping": [
      {
        "type": 0,
        "value": "Shopping"
      }
    ],
    "Icons.Snapchat": [
      {
        "type": 0,
        "value": "Snapchat"
      }
    ],
    "Icons.SocialHandle": [
      {
        "type": 0,
        "value": "SocialHandle"
      }
    ],
    "Icons.Spotify": [
      {
        "type": 0,
        "value": "Spotify"
      }
    ],
    "Icons.Star": [
      {
        "type": 0,
        "value": "Star"
      }
    ],
    "Icons.Telegram": [
      {
        "type": 0,
        "value": "Telegram"
      }
    ],
    "Icons.Threads": [
      {
        "type": 0,
        "value": "Threads"
      }
    ],
    "Icons.Tiktok": [
      {
        "type": 0,
        "value": "Tiktok"
      }
    ],
    "Icons.Timestamp": [
      {
        "type": 0,
        "value": "Timestamp"
      }
    ],
    "Icons.Triangle": [
      {
        "type": 0,
        "value": "Triangle"
      }
    ],
    "Icons.TriangleDown": [
      {
        "type": 0,
        "value": "TriangleDown"
      }
    ],
    "Icons.TriangleUp": [
      {
        "type": 0,
        "value": "TriangleUp"
      }
    ],
    "Icons.Tumblr": [
      {
        "type": 0,
        "value": "Tumblr"
      }
    ],
    "Icons.Twitter": [
      {
        "type": 0,
        "value": "X"
      }
    ],
    "Icons.Vero": [
      {
        "type": 0,
        "value": "VERO"
      }
    ],
    "Icons.Viber": [
      {
        "type": 0,
        "value": "Rakuten Viber"
      }
    ],
    "Icons.Video": [
      {
        "type": 0,
        "value": "Video"
      }
    ],
    "Icons.Vk": [
      {
        "type": 0,
        "value": "VKonkakte"
      }
    ],
    "Icons.VolumeHigh": [
      {
        "type": 0,
        "value": "Turn on the volume"
      }
    ],
    "Icons.VolumeMute": [
      {
        "type": 0,
        "value": "Turn off the volume"
      }
    ],
    "Icons.WeChat": [
      {
        "type": 0,
        "value": "WeChat"
      }
    ],
    "Icons.WebLink": [
      {
        "type": 0,
        "value": "Website Link"
      }
    ],
    "Icons.Weibo": [
      {
        "type": 0,
        "value": "Sina Weibo"
      }
    ],
    "Icons.Whatsapp": [
      {
        "type": 0,
        "value": "Whatsapp"
      }
    ],
    "Icons.Xing": [
      {
        "type": 0,
        "value": "Xing"
      }
    ],
    "Icons.YandexZen": [
      {
        "type": 0,
        "value": "Yandex.Zen"
      }
    ],
    "Icons.YouTube": [
      {
        "type": 0,
        "value": "YouTube"
      }
    ],
    "Icons.chevronFill": [
      {
        "type": 0,
        "value": "chevronFill"
      }
    ],
    "Icons.funny": [
      {
        "type": 0,
        "value": "Funny"
      }
    ],
    "Icons.someWhatFunny": [
      {
        "type": 0,
        "value": "Somewhat funny"
      }
    ],
    "Icons.unFunny": [
      {
        "type": 0,
        "value": "Unfunny"
      }
    ],
    "Icons.wavyarrow": [
      {
        "type": 0,
        "value": "Wavy Arrow"
      }
    ],
    "IdentityUnits.SignIn": [
      {
        "type": 0,
        "value": "Sign In"
      }
    ],
    "IframeEmbed.AriaLabel": [
      {
        "type": 0,
        "value": "Click button to go to: "
      },
      {
        "type": 1,
        "value": "name"
      }
    ],
    "IframeEmbed.ConsentBannerHeader": [
      {
        "type": 0,
        "value": "Content"
      }
    ],
    "IframeEmbed.DangerousDek": [
      {
        "type": 0,
        "value": "Listen to this story"
      }
    ],
    "IframeEmbed.Title": [
      {
        "type": 0,
        "value": "Embedded Frame"
      }
    ],
    "ImageSearchFilters.SearchPlaceholderDesktopPrefix": [
      {
        "type": 0,
        "value": "Try searching"
      }
    ],
    "ImageSearchFilters.SearchPlaceholderMobilePrefix": [
      {
        "type": 0,
        "value": "Try"
      }
    ],
    "ImageSlideShow.galleryLink": [
      {
        "type": 0,
        "value": "See the gallery"
      }
    ],
    "ImageSlideShow.lastSlideCTA": [
      {
        "type": 0,
        "value": "Explore the gallery"
      }
    ],
    "IngredientList.hedText": [
      {
        "type": 0,
        "value": "Ingredients"
      }
    ],
    "IngredientList.nutritionHedText": [
      {
        "type": 0,
        "value": "Nutrition Per Serving"
      }
    ],
    "InstagramEmbed.ConsentBannerHeader": [
      {
        "type": 0,
        "value": "Instagram content"
      }
    ],
    "InstructionList.StepText": [
      {
        "type": 0,
        "value": "Step"
      }
    ],
    "ItemCount.ItemTypeCharacter": [
      {
        "options": {
          "other": {
            "value": [
              {
                "offset": 0,
                "options": {
                  "one": {
                    "value": [
                      {
                        "type": 7
                      },
                      {
                        "type": 0,
                        "value": " character"
                      }
                    ]
                  },
                  "other": {
                    "value": [
                      {
                        "type": 7
                      },
                      {
                        "type": 0,
                        "value": " characters"
                      }
                    ]
                  }
                },
                "pluralType": "cardinal",
                "type": 6,
                "value": "count"
              }
            ]
          },
          "withMinCountLimit": {
            "value": [
              {
                "offset": 0,
                "options": {
                  "one": {
                    "value": [
                      {
                        "type": 7
                      },
                      {
                        "type": 0,
                        "value": " character"
                      }
                    ]
                  },
                  "other": {
                    "value": [
                      {
                        "type": 7
                      },
                      {
                        "type": 0,
                        "value": " characters"
                      }
                    ]
                  }
                },
                "pluralType": "cardinal",
                "type": 6,
                "value": "count"
              },
              {
                "type": 0,
                "value": " (at least "
              },
              {
                "offset": 0,
                "options": {
                  "one": {
                    "value": [
                      {
                        "type": 7
                      },
                      {
                        "type": 0,
                        "value": " character"
                      }
                    ]
                  },
                  "other": {
                    "value": [
                      {
                        "type": 7
                      },
                      {
                        "type": 0,
                        "value": " characters"
                      }
                    ]
                  }
                },
                "pluralType": "cardinal",
                "type": 6,
                "value": "minCount"
              },
              {
                "type": 0,
                "value": " are required)"
              }
            ]
          }
        },
        "type": 5,
        "value": "messageType"
      }
    ],
    "ItemCount.ItemTypeDefault": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Item"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Items"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "count"
      }
    ],
    "ItemCount.ItemTypeImage": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Image"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Images"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "count"
      }
    ],
    "ItemCount.ItemTypePhoto": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Photo"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Photos"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "count"
      }
    ],
    "ItemCount.ItemTypeSlide": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Slide"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Slides"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "count"
      }
    ],
    "ItemCount.ItemTypeVenue": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Venue"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Venues"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "count"
      }
    ],
    "JustWatchEmbed.PoweredBy": [
      {
        "type": 0,
        "value": "Powered by"
      }
    ],
    "Lightbox.CloseButtonIconLabel": [
      {
        "type": 0,
        "value": "Close Lightbox"
      }
    ],
    "Lightbox.ContentLabel": [
      {
        "type": 0,
        "value": "Photo Gallery"
      }
    ],
    "LiveStory.LoadMoreButtonLabel": [
      {
        "type": 0,
        "value": "Load More"
      }
    ],
    "LiveStory.LoadMoreLoadingLabel": [
      {
        "type": 0,
        "value": "Loading ..."
      }
    ],
    "LiveStory.feedADayAgoLabel": [
      {
        "type": 0,
        "value": "a day ago"
      }
    ],
    "LiveStory.feedAMinAgoLabel": [
      {
        "type": 0,
        "value": "a minute ago"
      }
    ],
    "LiveStory.feedAMonthAgoLabel": [
      {
        "type": 0,
        "value": "a month ago"
      }
    ],
    "LiveStory.feedAYearAgoLabel": [
      {
        "type": 0,
        "value": "a year ago"
      }
    ],
    "LiveStory.feedAnHourAgoLabel": [
      {
        "type": 0,
        "value": "an hour ago"
      }
    ],
    "LiveStory.feedFewSecondsAgoLabel": [
      {
        "type": 0,
        "value": "a few seconds ago"
      }
    ],
    "LiveStory.lastUpdatedTimePrefixLabel": [
      {
        "type": 0,
        "value": "Updated"
      }
    ],
    "MagazineBundlePage.magazineHeading": [
      {
        "type": 0,
        "value": "The Magazine"
      }
    ],
    "MagazineBundlePage.nextButton": [
      {
        "type": 0,
        "value": "Next"
      }
    ],
    "MagazineBundlePage.previousButton": [
      {
        "type": 0,
        "value": "Previous"
      }
    ],
    "MagazineDisclaimer.DisclaimerNoHed": [
      {
        "type": 0,
        "value": "Published in the print edition of the "
      },
      {
        "type": 1,
        "value": "issueDate"
      },
      {
        "type": 0,
        "value": ", issue."
      }
    ],
    "MagazineDisclaimer.DisclaimerWithHed": [
      {
        "type": 0,
        "value": "Published in the print edition of the "
      },
      {
        "type": 1,
        "value": "issueDate"
      },
      {
        "type": 0,
        "value": ", issue, with the headline “"
      },
      {
        "type": 1,
        "value": "hed"
      },
      {
        "type": 0,
        "value": ".”"
      }
    ],
    "MapPreview.MapAriaLabel": [
      {
        "type": 0,
        "value": "Location map of address"
      }
    ],
    "MapPreview.MapPreviewHeader": [
      {
        "type": 0,
        "value": "Location Map"
      }
    ],
    "MastodonEmbed.AriaLabelText": [
      {
        "type": 0,
        "value": "social media post"
      }
    ],
    "MastodonEmbed.ConsentBannerHeader": [
      {
        "type": 0,
        "value": "Mastodon content"
      }
    ],
    "MegaMenu.All": [
      {
        "type": 0,
        "value": "All"
      }
    ],
    "MegaMenu.MegaMenuButton": [
      {
        "type": 0,
        "value": "Close Mega Menu"
      }
    ],
    "MegaMenu.NavigationPrimaryAriaLabel": [
      {
        "type": 0,
        "value": "Primary"
      }
    ],
    "MegaMenu.SignInLinkText": [
      {
        "type": 0,
        "value": "Sign in"
      }
    ],
    "MegaMenu.VerboseClickOut": [
      {
        "type": 0,
        "value": "More"
      }
    ],
    "MenuList.unavailableFilters": [
      {
        "type": 0,
        "value": "Unavailable filters"
      }
    ],
    "MessageBanner.saveStory": [
      {
        "type": 0,
        "value": "Save story"
      }
    ],
    "MobileProductCard.CardAvailability": [
      {
        "type": 0,
        "value": "Multiple Buying Options Available"
      }
    ],
    "MobileProductCard.CardRating": [
      {
        "type": 0,
        "value": "Rating: "
      },
      {
        "type": 1,
        "value": "rating"
      },
      {
        "type": 0,
        "value": "/10"
      }
    ],
    "MobileProductCard.CtaText": [
      {
        "type": 0,
        "value": "Buy Now"
      }
    ],
    "Multipackages.ExploreInstead": [
      {
        "type": 0,
        "value": "Explore these instead"
      }
    ],
    "Multipackages.NoStories": [
      {
        "type": 0,
        "value": "No stories found for your search"
      }
    ],
    "NativeDisclaimer.Text": [
      {
        "type": 0,
        "value": "This article was published by The New Yorker Brand Studio for "
      },
      {
        "type": 1,
        "value": "sponsorName"
      },
      {
        "type": 0,
        "value": ". The editorial staff of The New Yorker had no role in this post's preparation."
      }
    ],
    "NativeShareButton.ButtonTitle": [
      {
        "type": 0,
        "value": "Share"
      }
    ],
    "Navigation.OneTrustButtonLabel": [
      {
        "type": 0,
        "value": "Do Not Sell My Personal Info"
      }
    ],
    "NewsFeed.LoadMoreNewsPreamble": [
      {
        "type": 0,
        "value": "Show More News"
      }
    ],
    "NewsLetterManagePageNewsLetterSubscribeForm.TypeMismatchMessage": [
      {
        "type": 0,
        "value": "Invalid email. Double check and try again."
      }
    ],
    "NewsletterManageContent.SecondaryOptinsDangerousLegend": [
      {
        "type": 0,
        "value": "Primary and Third Party Optins"
      }
    ],
    "NewsletterManageContent.SignUp": [
      {
        "type": 0,
        "value": "Sign up"
      }
    ],
    "NewsletterManageContent.SignUpMessage": [
      {
        "type": 0,
        "value": "You’re signed up."
      }
    ],
    "NewsletterManagePage.BadResponseServerMessage": [
      {
        "type": 0,
        "value": "Subscription failed: Bad response"
      }
    ],
    "NewsletterManagePage.EmptyNewsletterErrorMessage": [
      {
        "type": 0,
        "value": "Subscription failed: Please select a newsletter"
      }
    ],
    "NewsletterManagePage.UnknownErrorMessage": [
      {
        "type": 0,
        "value": "Subscription failed: Unknown error occurred"
      }
    ],
    "NewsletterManagePage.closeSubmitModelTextField": [
      {
        "type": 0,
        "value": "Go back"
      }
    ],
    "NewsletterManagePage.completeSignUp": [
      {
        "type": 0,
        "value": "Complete Sign Up"
      }
    ],
    "NewsletterManagePage.goBackFromPreviewButton": [
      {
        "type": 0,
        "value": "Go back"
      }
    ],
    "NewsletterManagePage.previewText": [
      {
        "type": 0,
        "value": "Preview"
      }
    ],
    "NewsletterManagePage.readPreviewButton": [
      {
        "type": 0,
        "value": "Read a preview"
      }
    ],
    "NewsletterManagePage.signedUpPopUpMessage": [
      {
        "type": 0,
        "value": "You’re signed up to this newsletter."
      }
    ],
    "NewsletterManagePage.ukPrimaryMarketingPermission": [
      {
        "type": 0,
        "value": "Sign up to receive emails from "
      },
      {
        "type": 1,
        "value": "brandName"
      },
      {
        "type": 0,
        "value": " about "
      },
      {
        "type": 1,
        "value": "brandName"
      },
      {
        "type": 0,
        "value": "’s products, promotions, and services."
      }
    ],
    "NewsletterManagePage.ukThirdPartyMarketingPermission": [
      {
        "type": 0,
        "value": "Sign up to receive marketing emails from "
      },
      {
        "type": 1,
        "value": "brandName"
      },
      {
        "type": 0,
        "value": " about special offers and promotions for other Condé Nast brands and our marketing partners."
      }
    ],
    "NewsletterManagePage.viewMoreNewsletters": [
      {
        "type": 0,
        "value": "View more newsletters"
      }
    ],
    "NewsletterOneClickForm.BadResponse": [
      {
        "type": 0,
        "value": "Bad response for signup newsletter"
      }
    ],
    "NewsletterOneClickForm.ErrorMessage": [
      {
        "type": 0,
        "value": "Subscription failed"
      }
    ],
    "NewsletterOneClickForm.TypeMismatchMessage": [
      {
        "type": 0,
        "value": "Invalid email. Double check and try again."
      }
    ],
    "NewsletterOneClickVerticalForm.BadResponse": [
      {
        "type": 0,
        "value": "Bad response for signup newsletter"
      }
    ],
    "NewsletterOneClickVerticalForm.ErrorMessage": [
      {
        "type": 0,
        "value": "Subscription failed"
      }
    ],
    "NewsletterOneClickVerticalForm.TypeMismatchMessage": [
      {
        "type": 0,
        "value": "Invalid email. Double check and try again."
      }
    ],
    "NewsletterSlice.DismissButton": [
      {
        "type": 0,
        "value": "Dismiss Newsletter Slice"
      }
    ],
    "NewsletterSlice.NewsletterSecondaryOptinsLegend": [
      {
        "type": 0,
        "value": "Consent checks"
      }
    ],
    "NowReading.SeriesNavigation": [
      {
        "type": 0,
        "value": "Now Reading"
      }
    ],
    "OverlayNavigation.OverlayNavigationButton": [
      {
        "type": 0,
        "value": "Close Navigation Menu"
      }
    ],
    "OverlayNavigation.OverlayNavigationPrimaryLinks": [
      {
        "type": 0,
        "value": "Primary"
      }
    ],
    "OverlayNavigation.OverlayNavigationSearchLabel": [
      {
        "type": 0,
        "value": "Search"
      }
    ],
    "OverlayNavigation.OverlayNavigationSecondaryLinks": [
      {
        "type": 0,
        "value": "Secondary"
      }
    ],
    "OverlayNavigation.OverlayNavigationSignInLabel": [
      {
        "type": 0,
        "value": "Sign In"
      }
    ],
    "OverlayNavigation.OverlayNavigationUtilityLinks": [
      {
        "type": 0,
        "value": "Utility"
      }
    ],
    "OverlayNavigation.OverlayNavigationWrapper": [
      {
        "type": 0,
        "value": "Overlay Navigation"
      }
    ],
    "PLPProductCard.AtRetailerNameComponentText": [
      {
        "type": 0,
        "value": "Shop at "
      },
      {
        "type": 1,
        "value": "sellerNameText"
      }
    ],
    "PLPProductCard.AtRetailerNameLabel": [
      {
        "type": 0,
        "value": "$ "
      },
      {
        "type": 1,
        "value": "finalPriceLabel"
      },
      {
        "type": 0,
        "value": " At "
      },
      {
        "type": 1,
        "value": "sellerNameText"
      }
    ],
    "PLPProductCard.BuyAt": [
      {
        "type": 0,
        "value": "Buy At "
      },
      {
        "type": 1,
        "value": "sellerNameText"
      }
    ],
    "PLPProductCard.ShopNowComponentText": [
      {
        "type": 0,
        "value": "Shop Now"
      }
    ],
    "PaginationModal.NextPage": [
      {
        "type": 0,
        "value": "Next"
      }
    ],
    "PaginationModal.PreviousPage": [
      {
        "type": 0,
        "value": "Previous"
      }
    ],
    "PaginationRow.NextPage": [
      {
        "type": 0,
        "value": "Next Page"
      }
    ],
    "PhotoBookmark.DefaultDesktopMessageBannerText": [
      {
        "type": 0,
        "value": "Click the icon to save a story to your account."
      }
    ],
    "PhotoBookmark.DefaultMobileMessageBannerText": [
      {
        "type": 0,
        "value": "Tap the icon to save a story to your account."
      }
    ],
    "PhotoBookmark.GalleryDesktopMessageBannerText": [
      {
        "type": 0,
        "value": "Click the icon to save an image to your account."
      }
    ],
    "PhotoBookmark.GalleryMobileMessageBannerText": [
      {
        "type": 0,
        "value": "Tap the icon to save an image to your account."
      }
    ],
    "PhotoBookmark.RunwayDesktopMessageBannerText": [
      {
        "type": 0,
        "value": "Hover over an image and click the icon to save it to your account."
      }
    ],
    "PhotoBookmark.RunwayMobileMessageBannerText": [
      {
        "type": 0,
        "value": "Tap the icon to save an image to your account."
      }
    ],
    "PhotoBookmark.SaveAlertSavedToBoardMessage": [
      {
        "type": 0,
        "value": "Go To Boards"
      }
    ],
    "PhotoBookmark.SaveAlertWithBoardName": [
      {
        "type": 0,
        "value": "Saved to"
      }
    ],
    "PhotoBookmark.SaveBookmarkAlertLink": [
      {
        "type": 0,
        "value": "Create a Board"
      }
    ],
    "PhotoBookmark.SaveBookmarkAlertText": [
      {
        "type": 0,
        "value": "Image saved"
      }
    ],
    "PhotoBookmark.SaveIconTitle": [
      {
        "type": 0,
        "value": "Save Image"
      }
    ],
    "PhotoBookmark.SavedIconTitle": [
      {
        "type": 0,
        "value": "Image saved"
      }
    ],
    "PhotoBookmark.SignInHed": [
      {
        "type": 0,
        "value": "Save images"
      }
    ],
    "PhotoBookmark.SignInHedSpanTag": [
      {
        "type": 0,
        "value": "to your Vogue account"
      }
    ],
    "PhotoBookmark.SignInMessage": [
      {
        "type": 0,
        "value": "Sign in to save runway and street style images, then easily revisit them on any device."
      }
    ],
    "PhotoVogueHomePage.bestOfPvText": [
      {
        "type": 0,
        "value": "Best of Photovogue"
      }
    ],
    "PhotoVogueHomePage.featured": [
      {
        "type": 0,
        "value": "featured"
      }
    ],
    "PhotoVogueHomePage.introductionText": [
      {
        "type": 0,
        "value": "Connecting artists, community and commerce through Condé Nast's global creative networks, we champion talent and influence visual literacy to help foster a more just, ethical and inclusive world."
      }
    ],
    "PhotoVogueHomePage.nationalitiesAuthorNameText": [
      {
        "type": 0,
        "value": "Countries represented"
      }
    ],
    "PhotoVogueHomePage.nationalitiesRubricNameText": [
      {
        "type": 0,
        "value": "Nationalities"
      }
    ],
    "PhotoVogueHomePage.news": [
      {
        "type": 0,
        "value": "news"
      }
    ],
    "PhotoVogueHomePage.photoCountText": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Photo"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Photos"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "photoCount"
      }
    ],
    "PhotoVogueHomePage.photoVogue": [
      {
        "type": 0,
        "value": "PhotoVogue"
      }
    ],
    "PhotoVogueHomePage.photograpersAuthorNameText": [
      {
        "type": 0,
        "value": "Participating photographers"
      }
    ],
    "PhotoVogueHomePage.photographersRubricNameText": [
      {
        "type": 0,
        "value": "Photographers"
      }
    ],
    "PhotoVogueHomePage.photosAuthorNameText": [
      {
        "type": 0,
        "value": "Photos selected by the editors"
      }
    ],
    "PhotoVogueHomePage.photosRubricNameText": [
      {
        "type": 0,
        "value": "Photos"
      }
    ],
    "PhotoVogueHomePage.picOfTheDay": [
      {
        "type": 0,
        "value": "PIC OF THE DAY"
      }
    ],
    "PhotoVogueHomePage.seeAllBestOf": [
      {
        "type": 0,
        "value": "See All Best Of"
      }
    ],
    "PhotoVogueHomePage.seeAllFeatured": [
      {
        "type": 0,
        "value": "SEE ALL featured"
      }
    ],
    "PhotoVogueHomePage.seeAllNews": [
      {
        "type": 0,
        "value": "See All News"
      }
    ],
    "PhotoVogueHomePage.seeAllPhotographers": [
      {
        "type": 0,
        "value": "See All Photographers"
      }
    ],
    "PhotoVogueHomePage.seeAllPicOfTheDay": [
      {
        "type": 0,
        "value": "SEE ALL PICS OF THE DAY"
      }
    ],
    "PhotoVogueHomePage.spotlightPhotographers": [
      {
        "type": 0,
        "value": "Spotlight Photographers"
      }
    ],
    "PhotoVogueHomePage.spotlightRubric": [
      {
        "type": 0,
        "value": "Spotlight"
      }
    ],
    "PhotoVogueHomePage.tickerText": [
      {
        "type": 0,
        "value": "We’re excited to open up contributions to video, illustration and digital art in the near future"
      }
    ],
    "PhotoVoguePhotographersFilter.placeholderText": [
      {
        "type": 0,
        "value": "Search by first or last name"
      }
    ],
    "PhotoVoguePhotographersFilter.searchButtonText": [
      {
        "type": 0,
        "value": "Search"
      }
    ],
    "PhotoVoguePhotographersPage.PhotosCount": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " photo"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " photos"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "count"
      }
    ],
    "PhotoVoguePhotographersPage.clearAllText": [
      {
        "type": 0,
        "value": "Clear All"
      }
    ],
    "PhotoVoguePhotographersPage.country": [
      {
        "type": 0,
        "value": "Country"
      }
    ],
    "PhotoVoguePhotographersPage.errorMessage": [
      {
        "type": 0,
        "value": "Sorry, something went wrong. Please refresh the page and try again."
      }
    ],
    "PhotoVoguePhotographersPage.genre": [
      {
        "type": 0,
        "value": "Genre"
      }
    ],
    "PhotoVoguePhotographersPage.isSpotlight": [
      {
        "type": 0,
        "value": "Spotlight"
      }
    ],
    "PhotoVoguePhotographersPage.loadMore": [
      {
        "type": 0,
        "value": "See More"
      }
    ],
    "PhotoVoguePhotographersPage.loading": [
      {
        "type": 0,
        "value": "Loading…"
      }
    ],
    "PhotoVoguePhotographersPage.orText": [
      {
        "type": 0,
        "value": "or"
      }
    ],
    "PhotoVoguePhotographersPage.photographerLabel": [
      {
        "type": 0,
        "value": "photographer"
      }
    ],
    "PhotoVoguePhotographersPage.photographersLabel": [
      {
        "type": 0,
        "value": "photographers"
      }
    ],
    "PhotoVoguePhotographersPage.spotlight": [
      {
        "type": 0,
        "value": "Spotlight"
      }
    ],
    "PhotoVoguePhotosPage.Filter": [
      {
        "type": 0,
        "value": "Filter"
      }
    ],
    "PhotoVoguePhotosPage.countPrefixText": [
      {
        "type": 0,
        "value": "Showing"
      }
    ],
    "PhotoVoguePhotosPage.errorMessage": [
      {
        "type": 0,
        "value": "Sorry, something went wrong. Please refresh the page and try again."
      }
    ],
    "PhotoVoguePhotosPage.loadMore": [
      {
        "type": 0,
        "value": "Load More"
      }
    ],
    "PhotoVoguePhotosPage.loading": [
      {
        "type": 0,
        "value": "Loading…"
      }
    ],
    "PhotoVoguePhotosPage.photoLabel": [
      {
        "type": 0,
        "value": "photo"
      }
    ],
    "PhotoVoguePhotosPage.photosLabel": [
      {
        "type": 0,
        "value": "photos"
      }
    ],
    "PhotovogueArtistProfilePage.ShowLessText": [
      {
        "type": 0,
        "value": "Show less"
      }
    ],
    "PhotovogueArtistProfilePage.ShowMoreText": [
      {
        "type": 0,
        "value": "Show more"
      }
    ],
    "PhotovogueArtistProfilePage.allPhotos": [
      {
        "type": 0,
        "value": "All photos:"
      }
    ],
    "PhotovogueArtistProfilePage.bestOfPhotoVogue": [
      {
        "type": 0,
        "value": "Best of PhotoVogue:"
      }
    ],
    "PhotovogueArtistProfilePage.genre": [
      {
        "type": 0,
        "value": "Genre:"
      }
    ],
    "PhotovogueArtistProfilePage.picOfTheDayVogueText": [
      {
        "type": 0,
        "value": "Pic of the Day:"
      }
    ],
    "PhotovogueArtistProfilePage.portfolio": [
      {
        "type": 0,
        "value": "Portfolio"
      }
    ],
    "PhotovogueArtistProfilePage.showMoreText": [
      {
        "type": 0,
        "value": "Show more"
      }
    ],
    "PhotovogueArtistProfilePage.spotlightTitle": [
      {
        "type": 0,
        "value": "Spotlight"
      }
    ],
    "PinterestEmbed.AriaLabelText": [
      {
        "type": 0,
        "value": "social media post"
      }
    ],
    "PinterestEmbed.ConsentBannerHeader": [
      {
        "type": 0,
        "value": "Pinterest content"
      }
    ],
    "PodcastDetailedPage.contextualHeader": [
      {
        "type": 0,
        "value": "You Might Like This"
      }
    ],
    "PodcastDetailedPage.primaryCTALabel": [
      {
        "type": 0,
        "value": "Start Listening Now"
      }
    ],
    "PodcastDetailedPage.relatedArticleHed": [
      {
        "type": 0,
        "value": "Related Articles"
      }
    ],
    "ProductCard.CardRating": [
      {
        "type": 0,
        "value": "Rating: "
      },
      {
        "type": 1,
        "value": "rating"
      },
      {
        "type": 0,
        "value": "/10"
      }
    ],
    "ProductEmbed.DefaultCtaText": [
      {
        "type": 0,
        "value": "Buy It"
      }
    ],
    "ProductEmbed.DefaultTextPreamble": [
      {
        "type": 0,
        "value": "Learn More"
      }
    ],
    "ProductEmbed.PriceWithNoSellerPreamble": [
      {
        "type": 0,
        "value": "Buy for "
      },
      {
        "type": 1,
        "value": "price"
      }
    ],
    "ProductEmbed.PriceWithSellerPreamble": [
      {
        "type": 1,
        "value": "price"
      },
      {
        "type": 0,
        "value": " at "
      },
      {
        "type": 1,
        "value": "sellerName"
      }
    ],
    "ProductEmbed.VenueCtaText": [
      {
        "type": 0,
        "value": "Book Now"
      }
    ],
    "ProductOffer.defaultPriceString": [
      {
        "type": 1,
        "value": "priceValue"
      },
      {
        "type": 0,
        "value": " "
      },
      {
        "type": 1,
        "value": "sellerName"
      }
    ],
    "ProductOffer.price": [
      {
        "type": 1,
        "value": "priceValue"
      },
      {
        "type": 0,
        "value": " at "
      },
      {
        "type": 1,
        "value": "sellerName"
      }
    ],
    "ProductOffer.productOffersaveBookmarkLabel": [
      {
        "type": 0,
        "value": "Save story"
      }
    ],
    "ProductOffer.variationDefaultCTA": [
      {
        "type": 0,
        "value": "Shop Now"
      }
    ],
    "ProductOffer.variationSellerNameString": [
      {
        "type": 0,
        "value": "Shop at"
      }
    ],
    "ProductSummaryGrid.DefaultProductSummaryGridTitle": [
      {
        "type": 0,
        "value": "Featured in this article"
      }
    ],
    "ProductSummaryGrid.GridTitle": [
      {
        "type": 0,
        "value": "Featured in this article"
      }
    ],
    "ProductSummaryGrid.ReadMore": [
      {
        "type": 0,
        "value": "Read more"
      }
    ],
    "ProductSummaryGrid.ShowLess": [
      {
        "type": 0,
        "value": "Show less"
      }
    ],
    "ProductSummaryGrid.ShowMore": [
      {
        "type": 0,
        "value": "Show more"
      }
    ],
    "ProsCons.ConsLabel": [
      {
        "type": 0,
        "value": "Cons →"
      }
    ],
    "ProsCons.ProsLabel": [
      {
        "type": 0,
        "value": "Pros →"
      }
    ],
    "Rating.RatingAriaLabel": [
      {
        "type": 0,
        "value": "Rating"
      }
    ],
    "RatingsForm.LoadingText": [
      {
        "type": 0,
        "value": "Loading..."
      }
    ],
    "RatingsForm.PreviousRatingText": [
      {
        "type": 0,
        "value": "You previously rated "
      },
      {
        "type": 1,
        "value": "RATING_SUBJECT"
      },
      {
        "type": 0,
        "value": "."
      }
    ],
    "RatingsForm.PromptText": [
      {
        "type": 0,
        "value": "How would you rate "
      },
      {
        "type": 1,
        "value": "RATING_SUBJECT"
      },
      {
        "type": 0,
        "value": "?"
      }
    ],
    "RatingsForm.SuccessText": [
      {
        "type": 0,
        "value": "Thanks for your feedback!"
      }
    ],
    "ReadMore.SeriesRecirc": [
      {
        "type": 0,
        "value": "Read more"
      }
    ],
    "ReadNext.SeriesRecirc": [
      {
        "type": 0,
        "value": "Read next"
      }
    ],
    "RecipePage.ActiveTime": [
      {
        "type": 0,
        "value": "Active Time"
      }
    ],
    "RecipePage.CooksNote": [
      {
        "type": 0,
        "value": "Cooks' Note"
      }
    ],
    "RecipePage.PrepTime": [
      {
        "type": 0,
        "value": "Prep Time"
      }
    ],
    "RecipePage.TotalTime": [
      {
        "type": 0,
        "value": "Total Time"
      }
    ],
    "RecipePage.Yield": [
      {
        "type": 0,
        "value": "Yield"
      }
    ],
    "RecipePage.info": [
      {
        "type": 0,
        "value": "Recipe information"
      }
    ],
    "RecipeProductCarousel.Title": [
      {
        "type": 0,
        "value": "What you’ll need"
      }
    ],
    "RecircList.AlsoOn": [
      {
        "type": 0,
        "value": "Also On "
      },
      {
        "type": 1,
        "value": "brandName"
      }
    ],
    "RecircList.ReadMore": [
      {
        "type": 0,
        "value": "Read More"
      }
    ],
    "RecircMostPopular.SectionTitle": [
      {
        "type": 0,
        "value": "Most Popular"
      }
    ],
    "RedditEmbed.AriaLabelText": [
      {
        "type": 0,
        "value": "social media post"
      }
    ],
    "RedditEmbed.ConsentBannerHeader": [
      {
        "type": 0,
        "value": "Reddit content"
      }
    ],
    "RelatedList.SectionTitle": [
      {
        "type": 0,
        "value": "Related Stories"
      }
    ],
    "RelatedVideo.HeaderText": [
      {
        "type": 0,
        "value": "Featured Video"
      }
    ],
    "ResponsiveCartoon.cartButtonMessage": [
      {
        "type": 0,
        "value": "Shop"
      }
    ],
    "ResponsiveCartoon.copiedLinkAlertMessage": [
      {
        "type": 0,
        "value": "Link copied"
      }
    ],
    "ResponsiveCartoon.copyLinkButtonMessage": [
      {
        "type": 0,
        "value": "Copy link to cartoon"
      }
    ],
    "ResponsiveCartoon.downloadButtonMessage": [
      {
        "type": 0,
        "value": "Download"
      }
    ],
    "ResponsiveCartoon.openCartoonGalleryButtonIconMessage": [
      {
        "type": 0,
        "value": "Open Gallery"
      }
    ],
    "ResponsiveCartoon.openCartoonGalleryButtonMessage": [
      {
        "type": 0,
        "value": "Open cartoon gallery"
      }
    ],
    "ResponsiveClip.ClipAriaLabel": [
      {
        "type": 0,
        "value": "Play/Pause"
      }
    ],
    "ResponsiveClip.ClipLabel": [
      {
        "type": 0,
        "value": "Play/Pause Button"
      }
    ],
    "ReviewForm.AlertMessageError": [
      {
        "type": 0,
        "value": "Your feedback wasn't posted due to some error, please try again."
      }
    ],
    "ReviewForm.AlertMessageSuccess": [
      {
        "type": 0,
        "value": "Thanks for your feedback!"
      }
    ],
    "ReviewForm.FakeInputPlaceholderText": [
      {
        "type": 0,
        "value": "Tell us what you think"
      }
    ],
    "ReviewForm.Hed": [
      {
        "type": 0,
        "value": "Leave a Review"
      }
    ],
    "ReviewForm.InvalidFieldErrorMessage": [
      {
        "type": 0,
        "value": "Required fields missing"
      }
    ],
    "ReviewForm.IsAnonymousCheckboxLabel": [
      {
        "type": 0,
        "value": "Share anonymously"
      }
    ],
    "ReviewForm.LocationFieldLabel": [
      {
        "type": 0,
        "value": "Where are you from?"
      }
    ],
    "ReviewForm.LocationFieldPlaceholder": [
      {
        "type": 0,
        "value": "Boston, MA"
      }
    ],
    "ReviewForm.ReviewTextFieldLabel": [
      {
        "type": 0,
        "value": "Your Review"
      }
    ],
    "ReviewForm.ReviewTextFieldPlaceholder": [
      {
        "type": 0,
        "value": "Let us know your thoughts…"
      }
    ],
    "ReviewForm.ReviewerInfoFieldLabel": [
      {
        "type": 0,
        "value": "Display Name"
      }
    ],
    "ReviewForm.ReviewerInfoFieldPlaceholder": [
      {
        "type": 0,
        "value": "Jane Doe"
      }
    ],
    "ReviewForm.SubmitButtonLabel": [
      {
        "type": 0,
        "value": "Submit"
      }
    ],
    "ReviewForm.SubmitButtonLabelLoading": [
      {
        "type": 0,
        "value": "Loading…"
      }
    ],
    "ReviewForm.WillPrepareAgainOption1Label": [
      {
        "type": 0,
        "value": "Yes"
      }
    ],
    "ReviewForm.WillPrepareAgainOption2Label": [
      {
        "type": 0,
        "value": "No"
      }
    ],
    "ReviewForm.WillPrepareAgainRadioLabel": [
      {
        "type": 0,
        "value": "Would you make this recipe again?"
      }
    ],
    "ReviewForm.nonLoggedInErrorMessage": [
      {
        "type": 0,
        "value": "Sign in or create an account to add comment."
      }
    ],
    "ReviewList.Loading": [
      {
        "type": 0,
        "value": "Loading…"
      }
    ],
    "ReviewList.ReviewListError": [
      {
        "type": 0,
        "value": "Sorry, more reviews can‘t be loaded right now. "
      },
      {
        "type": 1,
        "value": "br"
      },
      {
        "type": 0,
        "value": " Please try again later."
      }
    ],
    "ReviewList.ReviewReplyLabel": [
      {
        "type": 0,
        "value": "Reply"
      }
    ],
    "ReviewList.pinnedReviewLabel": [
      {
        "type": 0,
        "value": "Pinned by"
      }
    ],
    "ReviewList.showMoreButtonLabel": [
      {
        "type": 0,
        "value": "Show more comments"
      }
    ],
    "ReviewListContainer.UtilityLabel": [
      {
        "type": 0,
        "value": "Back to Top"
      }
    ],
    "ReviewNoteModal.CloseButtonAriaLabel": [
      {
        "type": 0,
        "value": "Close ReviewNoteModal Modal"
      }
    ],
    "ReviewNoteModal.CloseButtonLabel": [
      {
        "type": 0,
        "value": "close modal button label"
      }
    ],
    "ReviewNoteModal.Hed": [
      {
        "type": 0,
        "value": "Discard this comment?"
      }
    ],
    "ReviewNoteModal.continueLabel": [
      {
        "type": 0,
        "value": "No, still writing"
      }
    ],
    "ReviewNoteModal.dek": [
      {
        "type": 0,
        "value": "Everything you've written will be lost"
      }
    ],
    "ReviewNoteModal.discardLabel": [
      {
        "type": 0,
        "value": "Yes, discard it"
      }
    ],
    "ReviewNotes.AddNoteFailedToastMessage": [
      {
        "type": 0,
        "value": "Unable to add your comment. Please try again."
      }
    ],
    "ReviewNotesForm.ReviewerInfoFieldLabel": [
      {
        "type": 0,
        "value": "Commenting as:"
      }
    ],
    "ReviewNotesForm.ReviewerRatingLabel": [
      {
        "type": 0,
        "value": "Rate this"
      }
    ],
    "ReviewNotesForm.addNoteLabel": [
      {
        "type": 0,
        "value": "Add Comment"
      }
    ],
    "ReviewNotesForm.buttonLabel": [
      {
        "type": 0,
        "value": "Sign in or create account"
      }
    ],
    "ReviewNotesForm.cancelNoteLabel": [
      {
        "type": 0,
        "value": "Discard"
      }
    ],
    "ReviewNotesForm.defaultcommunityReviewText": [
      {
        "type": 0,
        "value": "Ask a question or leave a helpful tip, suggestion or opinion that is relevant and respectful for the community."
      }
    ],
    "ReviewNotesForm.invalidReviewNoteLength": [
      {
        "type": 0,
        "value": "Enter "
      },
      {
        "type": 1,
        "value": "min"
      },
      {
        "type": 0,
        "value": " characters or more to add a comment."
      }
    ],
    "ReviewNotesForm.maxCharLimitMet": [
      {
        "type": 0,
        "value": "_MAX_ character limit met"
      }
    ],
    "ReviewNotesForm.messageBannerText": [
      {
        "type": 0,
        "value": "Join the "
      },
      {
        "type": 1,
        "value": "brandName"
      },
      {
        "type": 0,
        "value": " community to add comments."
      }
    ],
    "ReviewNotesForm.remainingMaxCharLimit": [
      {
        "type": 0,
        "value": "_COUNT_ of _MAX_ character limit remaining"
      }
    ],
    "ReviewNotesForm.requiredField": [
      {
        "type": 0,
        "value": "Select a star rating to add a comment"
      }
    ],
    "ReviewNotesForm.reviewTagsLabel": [
      {
        "type": 0,
        "value": "TAG YOUR COMMENT (OPTIONAL)"
      }
    ],
    "ReviewNotesForm.reviewerFieldInfoIconText": [
      {
        "type": 0,
        "value": "Your username appears next to your comments and replies. Change it anytime in your Account."
      }
    ],
    "ReviewNotesForm.reviewerInfoIconButtonLabel": [
      {
        "type": 0,
        "value": "user name update message"
      }
    ],
    "ReviewNotesForm.textFieldLabel": [
      {
        "type": 0,
        "value": "Your Review"
      }
    ],
    "ReviewRatingData.ButtonLabel": [
      {
        "type": 0,
        "value": "Open rating explainer"
      }
    ],
    "ReviewRatingData.DataLabel": [
      {
        "type": 0,
        "value": "Rating:"
      }
    ],
    "ReviewReplyComment.HideRepliesLabel": [
      {
        "type": 0,
        "value": "Hide replies"
      }
    ],
    "ReviewReplyComment.LoadingRepliesLabel": [
      {
        "type": 0,
        "value": "Loading…"
      }
    ],
    "ReviewReplyComment.ReviewReplyCommentLabel": [
      {
        "type": 0,
        "value": "Reply"
      }
    ],
    "ReviewReplyComment.ReviewReplyLabel": [
      {
        "type": 0,
        "value": "Replying to"
      }
    ],
    "ReviewReplyComment.ShowMoreRepliesLabel": [
      {
        "type": 0,
        "value": "Show more replies"
      }
    ],
    "ReviewReplyNote.AddReplyFailedToastMessage": [
      {
        "type": 0,
        "value": "Unable to add your reply. Please try again."
      }
    ],
    "ReviewReplyNote.AddReplySuccessToastMessage": [
      {
        "type": 0,
        "value": "Reply added"
      }
    ],
    "ReviewReplyNote.CancelButtonLabel": [
      {
        "type": 0,
        "value": "Discard"
      }
    ],
    "ReviewReplyNote.ReplyButtonLabel": [
      {
        "type": 0,
        "value": "Reply"
      }
    ],
    "ReviewReplyNote.ReplyFieldPlaceHolder": [
      {
        "type": 0,
        "value": "Add your reply here"
      }
    ],
    "ReviewReplyNote.ReplyTextFieldLabel": [
      {
        "type": 0,
        "value": "Your Reply"
      }
    ],
    "ReviewReplyNote.ReviewFieldAlertLimitErrorText": [
      {
        "type": 0,
        "value": "_CHARACTER_LIMIT_CURRENT_ of _CHARACTER_LIMIT_ character limit remaining."
      }
    ],
    "ReviewReplyNote.ReviewFieldMaxLimitErrorText": [
      {
        "type": 0,
        "value": "_CHARACTER_LIMIT_ character limit met."
      }
    ],
    "ReviewReplyNote.ReviewFieldMinLimitErrorText": [
      {
        "type": 0,
        "value": "Enter 2 characters or more to add a reply."
      }
    ],
    "ReviewReplyNote.ReviewReplyLabel": [
      {
        "type": 0,
        "value": "Replying To:"
      }
    ],
    "ReviewSummary.SummaryLabel": [
      {
        "type": 0,
        "value": "TL;DR:"
      }
    ],
    "RunwayGalleryFilmstrip.FilmstripCollapsedMessage": [
      {
        "type": 0,
        "value": "Explore Collection"
      }
    ],
    "RunwayGalleryFilmstrip.FilmstripCollapsedMessageForNonCollectionGalleries": [
      {
        "type": 0,
        "value": "Explore Gallery"
      }
    ],
    "RunwayGalleryFilmstrip.FilmstripExpandedMessage": [
      {
        "type": 0,
        "value": "Hide Collection"
      }
    ],
    "RunwayGalleryFilmstrip.FilmstripExpandedMessageForNonCollectionGalleries": [
      {
        "type": 0,
        "value": "Hide Gallery"
      }
    ],
    "RunwayGalleryLookNumber.imageLookNumberPrefix": [
      {
        "type": 0,
        "value": "Look"
      }
    ],
    "RunwayGalleryPage.SaveBookmarkAlertLink": [
      {
        "type": 0,
        "value": "VIEW ALL"
      }
    ],
    "RunwayGalleryPage.SaveBookmarkAlertText": [
      {
        "type": 0,
        "value": "Image saved"
      }
    ],
    "ScoreBox.BestNewMusic": [
      {
        "type": 0,
        "value": "Best New Music"
      }
    ],
    "ScoreBox.BestNewReissue": [
      {
        "type": 0,
        "value": "Best New Reissue"
      }
    ],
    "ScoreBox.BestNewTrack": [
      {
        "type": 0,
        "value": "Best New Track"
      }
    ],
    "SearchBar.placeholder": [
      {
        "type": 0,
        "value": "Search for \"stir-fry\""
      }
    ],
    "SearchPage.ArtistTitle": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 0,
                "value": "Artist"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 0,
                "value": "Artists"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "count"
      }
    ],
    "SearchPage.AuthorTitle": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 0,
                "value": "Author"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 0,
                "value": "Authors"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "count"
      }
    ],
    "SearchPage.ClearAll": [
      {
        "type": 0,
        "value": "Clear All"
      }
    ],
    "SearchPage.FeatureTitle": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 0,
                "value": "Feature"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 0,
                "value": "Features"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "count"
      }
    ],
    "SearchPage.FilterResults": [
      {
        "type": 0,
        "value": "Filter Results"
      }
    ],
    "SearchPage.LoadMoreButtonLabel": [
      {
        "type": 0,
        "value": "More Stories"
      }
    ],
    "SearchPage.LoadMoreLoadingLabel": [
      {
        "type": 0,
        "value": "Loading ..."
      }
    ],
    "SearchPage.Loading": [
      {
        "type": 0,
        "value": "Loading ..."
      }
    ],
    "SearchPage.MoreStories": [
      {
        "type": 0,
        "value": "More Stories"
      }
    ],
    "SearchPage.NewsTitle": [
      {
        "type": 0,
        "value": "News"
      }
    ],
    "SearchPage.NoResultsFound": [
      {
        "type": 0,
        "value": "Sorry we can't display any results for those filtering options, please try again"
      }
    ],
    "SearchPage.NoResultsHed": [
      {
        "type": 0,
        "value": "No stories found for your search"
      }
    ],
    "SearchPage.ResultsHed": [
      {
        "type": 0,
        "value": "Search stories from "
      },
      {
        "type": 1,
        "value": "brandName"
      }
    ],
    "SearchPage.ResultsHedOnIssueDate": [
      {
        "type": 0,
        "value": "Search Results from "
      },
      {
        "type": 1,
        "value": "issueDate"
      },
      {
        "type": 0,
        "value": " issue"
      }
    ],
    "SearchPage.ReviewTitle": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 0,
                "value": "Review"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 0,
                "value": "Reviews"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "count"
      }
    ],
    "SearchPage.SearchButtonLabel": [
      {
        "type": 0,
        "value": "Search"
      }
    ],
    "SearchPage.SearchInputAriaLabel": [
      {
        "type": 0,
        "value": "search"
      }
    ],
    "SearchPage.SearchInputPlaceholder": [
      {
        "type": 0,
        "value": "Try \"Racial justice\""
      }
    ],
    "SearchPage.SortBy": [
      {
        "type": 0,
        "value": "Sort By"
      }
    ],
    "SearchPage.SortLabel": [
      {
        "type": 0,
        "value": "Sort by"
      }
    ],
    "SearchPage.ThePitchTitle": [
      {
        "type": 0,
        "value": "The Pitch"
      }
    ],
    "SearchPage.TrackTitle": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 0,
                "value": "Track"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 0,
                "value": "Tracks"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "count"
      }
    ],
    "SearchPage.VideoTitle": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 0,
                "value": "Video"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 0,
                "value": "Videos"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "count"
      }
    ],
    "SearchPage.noResultsContentHed": [
      {
        "type": 0,
        "value": "We didn't find any recipes, articles or videos for"
      }
    ],
    "SearchPage.noResultsCustomContentHed": [
      {
        "type": 0,
        "value": "We didn't find any results for"
      }
    ],
    "SearchPage.noResultsSubHed": [
      {
        "type": 0,
        "value": "We didn't find any"
      }
    ],
    "SearchPage.resultswithWordHed": [
      {
        "type": 0,
        "value": "Search results for"
      }
    ],
    "SearchPage.showAllArtists": [
      {
        "type": 0,
        "value": "SHOW ALL ARTISTS"
      }
    ],
    "SearchPage.showAllAuthors": [
      {
        "type": 0,
        "value": "SHOW ALL AUTHORS"
      }
    ],
    "SearchResultsIndicator.EmptyResultText": [
      {
        "type": 0,
        "value": "explore these instead"
      }
    ],
    "SearchResultsIndicator.ResultsTextWithTerm": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " story"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 1,
                "value": "moreResultsIndicator"
              },
              {
                "type": 0,
                "value": " stories"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "resultCount"
      },
      {
        "type": 0,
        "value": " about \""
      },
      {
        "type": 1,
        "value": "searchTerm"
      },
      {
        "type": 0,
        "value": "\""
      }
    ],
    "SearchResultsIndicator.ResultsTextWithoutTerm": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " story"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 1,
                "value": "moreResultsIndicator"
              },
              {
                "type": 0,
                "value": " results"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "resultCount"
      },
      {
        "type": 0,
        "value": " from "
      },
      {
        "type": 1,
        "value": "brandName"
      }
    ],
    "SearchResultsIndicator.ResultsWithPagination": [
      {
        "type": 1,
        "value": "pageStartIndex"
      },
      {
        "type": 0,
        "value": " - "
      },
      {
        "type": 1,
        "value": "pageEndIndex"
      },
      {
        "type": 0,
        "value": " of "
      },
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Result"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 1,
                "value": "moreResultsIndicator"
              },
              {
                "type": 0,
                "value": " Results"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "resultCount"
      }
    ],
    "SearchResultsIndicator.resultsList": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Result"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 1,
                "value": "moreResultsIndicator"
              },
              {
                "type": 0,
                "value": " Results"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "resultCount"
      }
    ],
    "SearchResultsIndicator.resultsListWithEntity": [
      {
        "type": 1,
        "value": "resultCount"
      },
      {
        "type": 1,
        "value": "moreResultsIndicator"
      },
      {
        "type": 0,
        "value": " "
      },
      {
        "type": 1,
        "value": "entity"
      }
    ],
    "SearchResultsIndicator.resultsListWithLocation": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " Result"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 1,
                "value": "moreResultsIndicator"
              },
              {
                "type": 0,
                "value": " Results"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "resultCount"
      },
      {
        "type": 0,
        "value": " in "
      },
      {
        "type": 1,
        "value": "location"
      }
    ],
    "SearchResultsIndicator.resultsListWithLocationAndEntity": [
      {
        "type": 1,
        "value": "resultCount"
      },
      {
        "type": 1,
        "value": "moreResultsIndicator"
      },
      {
        "type": 0,
        "value": " "
      },
      {
        "type": 1,
        "value": "entity"
      },
      {
        "type": 0,
        "value": " in "
      },
      {
        "type": 1,
        "value": "location"
      }
    ],
    "SearchResultsListPage.DekTextActivity": [
      {
        "type": 0,
        "value": "The best activities in "
      },
      {
        "type": 1,
        "value": "locationName"
      },
      {
        "type": 0,
        "value": ", as reviewed by our editors and contributors."
      }
    ],
    "SearchResultsListPage.DekTextHotel": [
      {
        "type": 0,
        "value": "The best hotels in "
      },
      {
        "type": 1,
        "value": "locationName"
      },
      {
        "type": 0,
        "value": ", as reviewed by our editors and contributors. We've stayed at some of the finest properties around the world, and these made the top of our list."
      }
    ],
    "SearchResultsListPage.HeaderText": [
      {
        "type": 1,
        "value": "pageHed"
      },
      {
        "type": 0,
        "value": " "
      },
      {
        "options": {
          "activity": {
            "value": [
              {
                "type": 0,
                "value": "activities"
              }
            ]
          },
          "hotel": {
            "value": [
              {
                "type": 0,
                "value": "hotels"
              }
            ]
          },
          "other": {
            "value": []
          }
        },
        "type": 5,
        "value": "contentType"
      }
    ],
    "SearchResultsListPage.Loading": [
      {
        "type": 0,
        "value": "Loading ..."
      }
    ],
    "SearchResultsListPage.MoreResults": [
      {
        "type": 0,
        "value": "Load More"
      }
    ],
    "SearchResultsListPage.NoResults": [
      {
        "type": 0,
        "value": "No results. Please try again."
      }
    ],
    "SearchResultsListPage.ResultsWithoutAnyFilter": [
      {
        "type": 0,
        "value": "We currently do not have any results that match your criteria. Here are design professionals who recently joined the Directory."
      }
    ],
    "SearchResultsListPage.ResultsWithoutProfession": [
      {
        "type": 0,
        "value": "We do not have any results that match your exact criteria. Here are other "
      },
      {
        "children": [
          {
            "type": 1,
            "value": "selectedCategory"
          }
        ],
        "type": 8,
        "value": "b"
      },
      {
        "type": 0,
        "value": " professionals in "
      },
      {
        "children": [
          {
            "type": 1,
            "value": "selectedState"
          }
        ],
        "type": 8,
        "value": "b"
      },
      {
        "type": 0,
        "value": "."
      }
    ],
    "SearchResultsListPage.ResultsWithoutProfessionAndALLState": [
      {
        "type": 0,
        "value": "We do not have any results that match your exact criteria. Here are other "
      },
      {
        "children": [
          {
            "type": 1,
            "value": "selectedCategory"
          }
        ],
        "type": 8,
        "value": "b"
      },
      {
        "type": 0,
        "value": " professionals."
      }
    ],
    "SearchResultsListPage.ResultsWithoutState": [
      {
        "type": 0,
        "value": "We do not have any results that match your exact criteria. Here are "
      },
      {
        "children": [
          {
            "type": 1,
            "value": "selectedCategory"
          }
        ],
        "type": 8,
        "value": "b"
      },
      {
        "type": 0,
        "value": " professionals in other locations."
      }
    ],
    "SearchResultsListPage.ResultsWithoutStateProfession": [
      {
        "type": 0,
        "value": "We do not have any results that match your exact criteria. Here are "
      },
      {
        "children": [
          {
            "type": 1,
            "value": "selectedCategory"
          }
        ],
        "type": 8,
        "value": "b"
      },
      {
        "type": 0,
        "value": " professionals in other locations."
      }
    ],
    "SearchResultsListPage.SearchButtonLabel": [
      {
        "type": 0,
        "value": "Search"
      }
    ],
    "SearchResultsListPage.SortBy": [
      {
        "type": 0,
        "value": "Sort By"
      }
    ],
    "SearchResultsListPage.searchResultsListPageHedText": [
      {
        "type": 0,
        "value": "Find an expert to help you with your next project"
      }
    ],
    "SearchResultsListPage.searchResultsListPageServiceHedText": [
      {
        "type": 0,
        "value": "Find an expert to help you with your next project"
      }
    ],
    "SearchableSummaryCollection.AsyncDropdownPlaceholder": [
      {
        "type": 0,
        "value": "Search by city or destination"
      }
    ],
    "SearchableSummaryCollection.ClickoutButtonLabel": [
      {
        "type": 0,
        "value": "View all "
      },
      {
        "type": 1,
        "value": "location"
      },
      {
        "type": 0,
        "value": " hotels"
      }
    ],
    "SearchableSummaryCollection.NoMatchesFoundLabel": [
      {
        "type": 0,
        "value": "No matches found"
      }
    ],
    "SearchableSummaryCollection.NoResultsMessage": [
      {
        "type": 0,
        "value": "Sorry, there are no results for your search - please try another location"
      }
    ],
    "SearchableSummaryCollection.SearchContainerHed": [
      {
        "type": 0,
        "value": "Where do you want to go?"
      }
    ],
    "SearchableSummaryCollection.SubmitButtonLabel": [
      {
        "type": 0,
        "value": "Search"
      }
    ],
    "SecondaryMenu.NavDropdownAssistiveLabel": [
      {
        "type": 0,
        "value": "Select international site"
      }
    ],
    "SecondaryMenu.NavDropdownHeader": [
      {
        "type": 0,
        "value": "Explore "
      },
      {
        "type": 1,
        "value": "rootBrandName"
      },
      {
        "type": 0,
        "value": " across the globe"
      }
    ],
    "SecondaryMenu.NavigationPrimaryAriaLabel": [
      {
        "type": 0,
        "value": "Primary"
      }
    ],
    "SecondaryMenu.SearchLinkText": [
      {
        "type": 0,
        "value": "Search"
      }
    ],
    "SecondaryMenu.SecondaryLinksAriaLabel": [
      {
        "type": 0,
        "value": "Secondary"
      }
    ],
    "SecondaryMenu.SignInLinkText": [
      {
        "type": 0,
        "value": "Sign in"
      }
    ],
    "SecondaryMenu.UtilityLinksAriaLabel": [
      {
        "type": 0,
        "value": "Utility"
      }
    ],
    "ShopifyCart.CartHeader": [
      {
        "type": 0,
        "value": "Shopping Cart"
      }
    ],
    "ShopifyCartEmpty.EmptyCartButtonLabel": [
      {
        "type": 0,
        "value": "GO SHOPPING"
      }
    ],
    "ShopifyCartEmpty.EmptyCartButtonLink": [
      {
        "type": 0,
        "value": "/shop/listing/all"
      }
    ],
    "ShopifyCartEmpty.EmptyCartHeader": [
      {
        "type": 0,
        "value": "YOUR SHOPPING CART IS EMPTY"
      }
    ],
    "ShopifyCartItem.CheckoutLabel": [
      {
        "type": 0,
        "value": "CHECK OUT"
      }
    ],
    "ShopifyCartItem.CheckoutText": [
      {
        "type": 0,
        "value": "Shipping and taxes calculated at checkout"
      }
    ],
    "ShopifyCartItem.RetailerLabel": [
      {
        "type": 0,
        "value": "Retailer:"
      }
    ],
    "ShopifyCartItem.SubtotalLabel": [
      {
        "type": 0,
        "value": "Subtotal"
      }
    ],
    "ShopifyProductDetail.addToCartLabel": [
      {
        "type": 0,
        "value": "Add To Cart"
      }
    ],
    "ShopifyProductDetail.quantityLabel": [
      {
        "type": 0,
        "value": "Quantity"
      }
    ],
    "ShoppableAssetEmbed.shoppingIconHoverText": [
      {
        "type": 0,
        "value": "Shop the look"
      }
    ],
    "SignInModal.CloseButtonAriaLabel": [
      {
        "type": 0,
        "value": "Close Sign In Modal"
      }
    ],
    "SignInModal.CloseButtonLabel": [
      {
        "type": 0,
        "value": "Close Sign In Modal"
      }
    ],
    "SignInModal.Hed": [
      {
        "type": 0,
        "value": "Save stories"
      }
    ],
    "SignInModal.HedSpanTag": [
      {
        "type": 0,
        "value": "with an account"
      }
    ],
    "SignInModal.OidcSignInLinkText": [
      {
        "type": 0,
        "value": "Sign in"
      }
    ],
    "SignInModal.OidcSignInText": [
      {
        "type": 0,
        "value": "Already have an account?"
      }
    ],
    "SignInModal.OidcSignUpButtonLabel": [
      {
        "type": 0,
        "value": "Create account"
      }
    ],
    "SignOutButton.SignOut": [
      {
        "type": 0,
        "value": "Sign Out"
      }
    ],
    "SimpleNavigation.SearchLabel": [
      {
        "type": 0,
        "value": "Search"
      }
    ],
    "SiteFooter.Dropdown": [
      {
        "type": 0,
        "value": "Select international site"
      }
    ],
    "SiteFooter.NoticesContainer": [
      {
        "type": 0,
        "value": "Notices"
      }
    ],
    "SiteFooter.OneTrustButtonLabel": [
      {
        "type": 0,
        "value": "Do Not Sell My Personal Info"
      }
    ],
    "SiteHeader.ScrollingNavigation": [
      {
        "type": 0,
        "value": "Primary"
      }
    ],
    "SiteHeader.UtilityNavigation": [
      {
        "type": 0,
        "value": "Utility"
      }
    ],
    "SmallProductCard.AtRetailerNameComponentText": [
      {
        "type": 0,
        "value": "At "
      },
      {
        "type": 1,
        "value": "retailerNameText"
      }
    ],
    "SmallProductCard.AtRetailerNameLabel": [
      {
        "type": 1,
        "value": "finalPriceLabel"
      },
      {
        "type": 0,
        "value": " At "
      },
      {
        "type": 1,
        "value": "retailerNameText"
      }
    ],
    "SmallProductCard.BuyAt": [
      {
        "type": 0,
        "value": "Buy At "
      },
      {
        "type": 1,
        "value": "retailerNameText"
      }
    ],
    "SplitScreenContentHeader.RatingLinkLabel": [
      {
        "type": 0,
        "value": "Read Reviews"
      }
    ],
    "SplitScreenContentHeader.VariousArtists": [
      {
        "type": 0,
        "value": "Various Artists"
      }
    ],
    "SponsoredContentHeader.BylineAdvertisementFeatureWith": [
      {
        "type": 0,
        "value": "Advertisement Feature With"
      }
    ],
    "SponsoredContentHeader.BylineAdvertising": [
      {
        "type": 0,
        "value": "Advertising"
      }
    ],
    "SponsoredContentHeader.BylineBrandPresentsAdvertiser": [
      {
        "type": 1,
        "value": "brandName"
      },
      {
        "type": 0,
        "value": " Presents"
      }
    ],
    "SponsoredContentHeader.BylineBrandXAdvertiser": [
      {
        "type": 1,
        "value": "brandName"
      },
      {
        "type": 0,
        "value": " X"
      }
    ],
    "SponsoredContentHeader.BylineBrandedContent": [
      {
        "type": 0,
        "value": "Branded Content By"
      }
    ],
    "SponsoredContentHeader.BylineCreated": [
      {
        "type": 0,
        "value": "Created By "
      },
      {
        "type": 1,
        "value": "brandName"
      },
      {
        "type": 0,
        "value": " For"
      }
    ],
    "SponsoredContentHeader.BylineInCollaboration": [
      {
        "type": 0,
        "value": "In Collaboration With"
      }
    ],
    "SponsoredContentHeader.BylineInPartnership": [
      {
        "type": 0,
        "value": "In Partnership With"
      }
    ],
    "SponsoredContentHeader.BylineOriginalContentBy": [
      {
        "type": 0,
        "value": "Original Content By"
      }
    ],
    "SponsoredContentHeader.BylinePR": [
      {
        "type": 0,
        "value": "PR"
      }
    ],
    "SponsoredContentHeader.BylinePaidPost": [
      {
        "type": 0,
        "value": "PAID POST"
      }
    ],
    "SponsoredContentHeader.BylinePaidPostByAdvertiser": [
      {
        "type": 0,
        "value": "Paid Post by "
      },
      {
        "type": 1,
        "value": "sponsorName"
      },
      {
        "type": 0,
        "value": ", Brought to you By Business Reporter"
      }
    ],
    "SponsoredContentHeader.BylinePresentedByAdvertiser": [
      {
        "type": 0,
        "value": "Presented By"
      }
    ],
    "SponsoredContentHeader.BylineProduced": [
      {
        "type": 0,
        "value": "Produced By"
      }
    ],
    "SponsoredContentHeader.BylineProducedByAdvertiser": [
      {
        "type": 0,
        "value": "Produced By"
      }
    ],
    "SponsoredContentHeader.BylineProducedByBrand": [
      {
        "type": 0,
        "value": "Produced By "
      },
      {
        "type": 1,
        "value": "brandName"
      },
      {
        "type": 0,
        "value": " With"
      }
    ],
    "SponsoredContentHeader.BylinePromotedByAdvertiser": [
      {
        "type": 0,
        "value": "Promoted by"
      }
    ],
    "SponsoredContentHeader.BylinePromotion": [
      {
        "type": 0,
        "value": "Promotion"
      }
    ],
    "SponsoredContentHeader.BylinePublishedByAdvertiser": [
      {
        "type": 0,
        "value": "Published By"
      }
    ],
    "SponsoredContentHeader.BylineSponsored": [
      {
        "type": 0,
        "value": "Sponsored content"
      }
    ],
    "SponsoredContentHeader.BylineSponsoredBy": [
      {
        "type": 0,
        "value": "Sponsored By"
      }
    ],
    "SponsoredContentHeader.BylineSponsoredContent": [
      {
        "type": 0,
        "value": "Sponsored Content By"
      }
    ],
    "SponsoredContentHeader.BylineTogetherWith": [
      {
        "type": 0,
        "value": "Together with"
      }
    ],
    "SponsoredContentHeader.SponsoredLinkCTA": [
      {
        "type": 0,
        "value": "Click to go to "
      },
      {
        "type": 1,
        "value": "sponsorName"
      },
      {
        "type": 0,
        "value": "'s website"
      }
    ],
    "SponsoredContentHeader.bylineAd": [
      {
        "type": 0,
        "value": "Ad"
      }
    ],
    "SponsoredContentHeader.bylineAdvertisementByAdvertiser": [
      {
        "type": 0,
        "value": "Advertisement By"
      }
    ],
    "SponsoredContentHeader.bylineAffiliatePartner": [
      {
        "type": 0,
        "value": "Affiliate Partner"
      }
    ],
    "SponsoredContentHeader.bylineInPartnershipWithAdvertiser": [
      {
        "type": 0,
        "value": "In Partnership With"
      }
    ],
    "SponsoredContentHeader.bylinePaidPartnershipWithAdvertiser": [
      {
        "type": 0,
        "value": "Paid Partnership With"
      }
    ],
    "SponsoredContentHeader.bylinePaidPromotionByAdvertiser": [
      {
        "type": 0,
        "value": "Paid Promotion By"
      }
    ],
    "SponsoredContentHeader.bylineSpecialFeature": [
      {
        "type": 0,
        "value": "Special Feature"
      }
    ],
    "SponsoredContentHeader.bylineSponsoredByAdvertiser": [
      {
        "type": 0,
        "value": "Sponsored By"
      }
    ],
    "StackedNavigation.DrawerLabel": [
      {
        "type": 0,
        "value": "Navigation and Sign Up Menu"
      }
    ],
    "StackedNavigation.MenuButton": [
      {
        "type": 0,
        "value": "Open Navigation Menu"
      }
    ],
    "StackedNavigation.OpenSearchMenuLabel": [
      {
        "type": 0,
        "value": "Open Search Menu"
      }
    ],
    "StackedNavigation.PrimaryLinksLabel": [
      {
        "type": 0,
        "value": "Primary"
      }
    ],
    "StackedNavigation.ProfileLinkLabel": [
      {
        "type": 0,
        "value": "My Profile"
      }
    ],
    "StackedNavigation.SearchLabel": [
      {
        "type": 0,
        "value": "Search"
      }
    ],
    "StackedNavigation.SubscribeLabel": [
      {
        "type": 0,
        "value": "Subscribe"
      }
    ],
    "StackedNavigation.UtilityLinksLabel": [
      {
        "type": 0,
        "value": "Utility"
      }
    ],
    "StandardNavigation.AccountLabel": [
      {
        "type": 0,
        "value": "My Account"
      }
    ],
    "StandardNavigation.Drawer": [
      {
        "type": 0,
        "value": "Navigation and Sign Up Menu"
      }
    ],
    "StandardNavigation.MenuButton": [
      {
        "type": 0,
        "value": "Open Navigation Menu"
      }
    ],
    "StandardNavigation.OpenSearchMenuLabel": [
      {
        "type": 0,
        "value": "Open Search Menu"
      }
    ],
    "StandardNavigation.SearchLabel": [
      {
        "type": 0,
        "value": "Search"
      }
    ],
    "StandardNavigation.SecondaryLinksLabel": [
      {
        "type": 0,
        "value": "Secondary"
      }
    ],
    "StandardNavigation.ShoppingCartAriaLabel": [
      {
        "type": 0,
        "value": "item(s) in Cart"
      }
    ],
    "StandardNavigation.ShoppingCartLabel": [
      {
        "type": 0,
        "value": "Shopping Cart"
      }
    ],
    "StandardNavigation.SignInLabel": [
      {
        "type": 0,
        "value": "Sign In"
      }
    ],
    "StandardNavigation.UtilityLinksLabel": [
      {
        "type": 0,
        "value": "Utility"
      }
    ],
    "StandardNavigation.saveBookmarkLabel": [
      {
        "type": 0,
        "value": "Save story"
      }
    ],
    "SummaryCarousel.seeMoreAriaLabel": [
      {
        "type": 0,
        "value": "See more videos"
      }
    ],
    "SummaryCollageThree.seeMore": [
      {
        "type": 0,
        "value": "See More Videos"
      }
    ],
    "SummaryCollectionSplitColumns.GuideItemHed": [
      {
        "type": 1,
        "value": "location"
      },
      {
        "type": 0,
        "value": " Travel Guide"
      }
    ],
    "SummaryCollectionSplitColumns.RecommendedTitle": [
      {
        "type": 0,
        "value": "Recommended "
      },
      {
        "type": 1,
        "value": "recommendedType"
      }
    ],
    "SummaryCollectionSplitColumns.ViewAllButton": [
      {
        "type": 0,
        "value": "View All "
      },
      {
        "type": 1,
        "value": "location"
      },
      {
        "type": 0,
        "value": " "
      },
      {
        "type": 1,
        "value": "recommendedType"
      }
    ],
    "SummaryItem.BusinessProfileCTAText": [
      {
        "type": 0,
        "value": "View Profile"
      }
    ],
    "SummaryItem.DefaultCTAText": [
      {
        "type": 0,
        "value": "Book Now"
      }
    ],
    "SummaryItem.DekReadMoreText": [
      {
        "type": 0,
        "value": "Read full review"
      }
    ],
    "SummaryItem.FuturePremiereLabel": [
      {
        "type": 0,
        "value": "PREMIERES"
      }
    ],
    "SummaryItem.LiveVideoLabel": [
      {
        "type": 0,
        "value": "live"
      }
    ],
    "SummaryItem.MoreInfoAndEpisodesPodcastCTA": [
      {
        "type": 0,
        "value": "More Info and Episodes"
      }
    ],
    "SummaryItem.NowShoppingLabel": [
      {
        "type": 0,
        "value": "Now Shopping"
      }
    ],
    "SummaryItem.PastPremiereLabel": [
      {
        "type": 0,
        "value": "PREMIERED"
      }
    ],
    "SummaryItem.ReadMore": [
      {
        "type": 0,
        "value": "Read More"
      }
    ],
    "SummaryItem.ShopNowCTA": [
      {
        "type": 0,
        "value": "Shop Now"
      }
    ],
    "SummaryItem.Slides": [
      {
        "offset": 0,
        "options": {
          "one": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " slide"
              }
            ]
          },
          "other": {
            "value": [
              {
                "type": 7
              },
              {
                "type": 0,
                "value": " slides"
              }
            ]
          }
        },
        "pluralType": "cardinal",
        "type": 6,
        "value": "slidesCount"
      }
    ],
    "SummaryItem.SponsoredContent": [
      {
        "type": 0,
        "value": "Sponsored Content"
      }
    ],
    "SummaryItem.StartListeningNowPodcastCTA": [
      {
        "type": 0,
        "value": "Start Listening Now"
      }
    ],
    "SummaryItem.TodayLabel": [
      {
        "type": 0,
        "value": "TODAY"
      }
    ],
    "SummaryItem.VenueSellerPreviewText": [
      {
        "type": 0,
        "value": "Powered By:"
      }
    ],
    "SummaryItemFeatured.FeaturedTitle": [
      {
        "type": 0,
        "value": "Featured"
      }
    ],
    "SummarySpotlight.ContinueReading": [
      {
        "type": 0,
        "value": "Continue reading »"
      }
    ],
    "SummarySpotlight.SelectedStories": [
      {
        "type": 0,
        "value": "Selected Stories"
      }
    ],
    "TagCloud.SectionHeader": [
      {
        "type": 0,
        "value": "Topics"
      }
    ],
    "TagPage.ClearAll": [
      {
        "type": 0,
        "value": "Clear All"
      }
    ],
    "TagPage.FilterDrawer": [
      {
        "type": 0,
        "value": "matching results"
      }
    ],
    "TagPage.FilterDrawer.FilterApplyActionButton": [
      {
        "type": 0,
        "value": "Apply"
      }
    ],
    "TagPage.FilterDrawer.FilterCancelActionButton": [
      {
        "type": 0,
        "value": "Cancel"
      }
    ],
    "TagPage.FilterResults": [
      {
        "type": 0,
        "value": "Filter Results"
      }
    ],
    "TagPage.Items": [
      {
        "type": 0,
        "value": "items"
      }
    ],
    "TagPage.Loading": [
      {
        "type": 0,
        "value": "Loading ..."
      }
    ],
    "TagPage.MoreStories": [
      {
        "type": 0,
        "value": "More Stories"
      }
    ],
    "TagPage.NoResultsFound": [
      {
        "type": 0,
        "value": "Sorry we can't display any results for those filtering options, please try again"
      }
    ],
    "TagPage.SortBy": [
      {
        "type": 0,
        "value": "Sort By"
      }
    ],
    "TextField.MultiLineErrorText": [
      {
        "type": 0,
        "value": "Use at least _MIN_ characters and a maximum of _MAX_."
      }
    ],
    "TextField.multiLineUpperLimitErrorText": [
      {
        "type": 0,
        "value": "Use maximum of _MAX_ characters only"
      }
    ],
    "ThreadsEmbed.ConsentBannerHeader": [
      {
        "type": 0,
        "value": "Threads content"
      }
    ],
    "TiktokEmbed.ConsentBannerHeader": [
      {
        "type": 0,
        "value": "TikTok content"
      }
    ],
    "TopStory.toutHead": [
      {
        "children": [
          {
            "type": 0,
            "value": "Also today . . ."
          }
        ],
        "type": 8,
        "value": "i"
      }
    ],
    "TwitterEmbed.ConsentBannerHeader": [
      {
        "type": 0,
        "value": "X content"
      }
    ],
    "TwitterEmbed.EmbedContainer": [
      {
        "type": 0,
        "value": "social media post"
      }
    ],
    "UnifiedProductCard.DefaultOfferCtaText": [
      {
        "type": 0,
        "value": "Shop Now"
      }
    ],
    "UnifiedProductCard.UnifiedProductCardAmazonPrimeExclusiveLabel": [
      {
        "type": 0,
        "value": "Amazon Prime Deal"
      }
    ],
    "UnifiedProductCard.UnifiedProductCardConsLabel": [
      {
        "type": 0,
        "value": "Cons"
      }
    ],
    "UnifiedProductCard.UnifiedProductCardProsConsTitle": [
      {
        "type": 0,
        "value": "Pros & Cons"
      }
    ],
    "UnifiedProductCard.UnifiedProductCardProsLabel": [
      {
        "type": 0,
        "value": "Pros"
      }
    ],
    "UnifiedProductCard.UnifiedProductCardRatingTitle": [
      {
        "type": 0,
        "value": "OUR RATING:"
      }
    ],
    "UserNameModal.CloseButtonLabel": [
      {
        "type": 0,
        "value": "Close User Name"
      }
    ],
    "UserNameModal.Dek": [
      {
        "type": 0,
        "value": "Your username will appear next to any comments and replies you add."
      }
    ],
    "UserNameModal.ErrorMessage": [
      {
        "type": 0,
        "value": "Unable to save username. Please try again."
      }
    ],
    "UserNameModal.Hed": [
      {
        "type": 0,
        "value": "Create Username"
      }
    ],
    "UserNameModal.SubmitButtonLabel": [
      {
        "type": 0,
        "value": "Save Username"
      }
    ],
    "UserNameModal.SuccessMessage": [
      {
        "type": 0,
        "value": "Your username is saved."
      }
    ],
    "UserNameModal.UserNameModalAssistiveText": [
      {
        "type": 0,
        "value": "Usernames must be between 2 and 23 characters and can only include letters, numbers and underscores (_)."
      }
    ],
    "UserNameModal.alreadyTakenError": [
      {
        "type": 0,
        "value": "This Username is already taken."
      }
    ],
    "UserNameModal.lengthError": [
      {
        "type": 0,
        "value": "Usernames must be between 2 and 23 characters."
      }
    ],
    "UserNameModal.specialCharError": [
      {
        "type": 0,
        "value": "Usernames can only include letters, numbers and underscores (_)."
      }
    ],
    "UserProfileForm.countryFieldLabel": [
      {
        "type": 0,
        "value": "Country"
      }
    ],
    "UserProfileForm.countryRequiredErrorMsg": [
      {
        "type": 0,
        "value": "Select your country."
      }
    ],
    "UserProfileForm.firstNameFieldLabel": [
      {
        "type": 0,
        "value": "First name"
      }
    ],
    "UserProfileForm.firstNameRequiredErrorMsg": [
      {
        "type": 0,
        "value": "Enter your first name."
      }
    ],
    "UserProfileForm.lastNameFieldLabel": [
      {
        "type": 0,
        "value": "Last name"
      }
    ],
    "UserProfileForm.lastNameRequiredErrorMsg": [
      {
        "type": 0,
        "value": "Enter your last name."
      }
    ],
    "UserProfileForm.phoneNumberFieldLabel": [
      {
        "type": 0,
        "value": "Phone number"
      }
    ],
    "UserProfileForm.phoneNumberLengthErrorMsg": [
      {
        "type": 0,
        "value": "Your phone number should be ten digits."
      }
    ],
    "UserProfileForm.phoneNumberNonUSLengthErrorMsg": [
      {
        "type": 0,
        "value": "Your phone number should be at least ten digits."
      }
    ],
    "UserProfileForm.phoneNumberNumericErrorMsg": [
      {
        "type": 0,
        "value": "Your phone number should consist of only numerical digits."
      }
    ],
    "UserProfileForm.phoneNumberRequiredErrorMsg": [
      {
        "type": 0,
        "value": "Enter your phone number."
      }
    ],
    "UserProfileForm.serverErrorMessageText": [
      {
        "type": 0,
        "value": "There was a problem saving your information. Please try again."
      }
    ],
    "UserProfileForm.stateFieldLabel": [
      {
        "type": 0,
        "value": "State / Province"
      }
    ],
    "UserProfileForm.stateRequiredErrorMsg": [
      {
        "type": 0,
        "value": "Select your state / province."
      }
    ],
    "UserProfileForm.submitButtonLabel": [
      {
        "type": 0,
        "value": "Save"
      }
    ],
    "UserProfileForm.termsAndConditionText": [
      {
        "type": 0,
        "value": "By submitting a caption, you agree to our "
      },
      {
        "children": [
          {
            "type": 0,
            "value": "User Agreement"
          }
        ],
        "type": 8,
        "value": "a"
      },
      {
        "type": 0,
        "value": " and "
      },
      {
        "children": [
          {
            "type": 0,
            "value": "Privacy Policy & Cookie Statement."
          }
        ],
        "type": 8,
        "value": "b"
      }
    ],
    "UtilityNavigation.AccountDropdown": [
      {
        "type": 0,
        "value": "Account"
      }
    ],
    "UtilityNavigation.AccountDropdownAssistive": [
      {
        "type": 0,
        "value": "Account Navigation"
      }
    ],
    "UtilityNavigation.MarketSwitcherLabel": [
      {
        "type": 0,
        "value": "Country"
      }
    ],
    "UtilityNavigation.SearchLabel": [
      {
        "type": 0,
        "value": "Search"
      }
    ],
    "UtilityNavigation.ShoppingCartAriaLabel": [
      {
        "type": 0,
        "value": "item(s) in Cart"
      }
    ],
    "UtilityNavigation.ShoppingCartLabel": [
      {
        "type": 0,
        "value": "Shopping Cart"
      }
    ],
    "UtilityNavigation.SignInLabel": [
      {
        "type": 0,
        "value": "Sign In"
      }
    ],
    "UtilityNavigation.SignOut": [
      {
        "type": 0,
        "value": "Sign Out"
      }
    ],
    "UtilityNavigation.UtilityNavigationButton": [
      {
        "type": 0,
        "value": "Open Navigation Menu"
      }
    ],
    "UtilityValidationDescription.Heading": [
      {
        "type": 0,
        "value": "Errors"
      }
    ],
    "VenuePage.BylinePreamble": [
      {
        "type": 0,
        "value": "Reviewed by"
      }
    ],
    "VenuePage.DefaultCTAText": [
      {
        "type": 0,
        "value": "Book Now"
      }
    ],
    "VenuePage.FilterableListHed": [
      {
        "type": 0,
        "value": "More To Discover"
      }
    ],
    "VenuePage.SectionTitleHed": [
      {
        "type": 0,
        "value": "Photos"
      }
    ],
    "VenuePage.VenueSellerPreviewText": [
      {
        "type": 0,
        "value": "Powered By:"
      }
    ],
    "VersoCommerceCollectionCurated.FilterBy.Brand": [
      {
        "type": 0,
        "value": "Designer"
      }
    ],
    "VersoCommerceCollectionCurated.FilterBy.Category": [
      {
        "type": 0,
        "value": "Type"
      }
    ],
    "VersoCommerceCollectionCurated.FilterBy.Color": [
      {
        "type": 0,
        "value": "Color"
      }
    ],
    "VersoCommerceCollectionCurated.FilterBy.Size": [
      {
        "type": 0,
        "value": "Size"
      }
    ],
    "VersoCommerceCollectionCurated.FilterBy.StorefrontBundle": [
      {
        "type": 0,
        "value": "Category"
      }
    ],
    "VersoCommerceCollectionCurated.FilterBy.Type": [
      {
        "type": 0,
        "value": "Type"
      }
    ],
    "VersoCommerceCollectionCurated.Items": [
      {
        "type": 0,
        "value": "Items"
      }
    ],
    "VersoCommerceCollectionCurated.SortBy.Featured": [
      {
        "type": 0,
        "value": "Featured"
      }
    ],
    "VersoCommerceCollectionCurated.SortBy.HighestPrice": [
      {
        "type": 0,
        "value": "Highest Price"
      }
    ],
    "VersoCommerceCollectionCurated.SortBy.LowestPrice": [
      {
        "type": 0,
        "value": "Lowest Price"
      }
    ],
    "VersoCommerceCollectionCurated.SortBy.MostRecent": [
      {
        "type": 0,
        "value": "New Arrivals"
      }
    ],
    "VersoCommerceCollectionCurated.SortBy.Popular": [
      {
        "type": 0,
        "value": "Most Wanted"
      }
    ],
    "VersoFeatures.viewAllButton": [
      {
        "type": 0,
        "value": "View All"
      }
    ],
    "VersoFilterableSummaryList.CTAMessage": [
      {
        "type": 0,
        "value": "See more "
      },
      {
        "type": 1,
        "value": "groupName"
      },
      {
        "type": 0,
        "value": " recipes"
      }
    ],
    "VersoIssueFeature.IssueFeatureLabel": [
      {
        "type": 0,
        "value": "Table of Contents »"
      }
    ],
    "VideoWrapper.headerText": [
      {
        "type": 0,
        "value": "WATCH"
      }
    ],
    "VideoWrapper.headerTextRelatedOverride": [
      {
        "type": 0,
        "value": "Featured Video"
      }
    ],
    "VideoWrapper.moreLink": [
      {
        "type": 0,
        "value": "More "
      },
      {
        "type": 1,
        "value": "brandName"
      },
      {
        "type": 0,
        "value": " Videos"
      }
    ],
    "venueFeatureList.venueBar": [
      {
        "type": 0,
        "value": "Bar"
      }
    ],
    "venueFeatureList.venueDetox": [
      {
        "type": 0,
        "value": "Detox"
      }
    ],
    "venueFeatureList.venueGolf": [
      {
        "type": 0,
        "value": "Golf"
      }
    ],
    "venueFeatureList.venueLocationMap": [
      {
        "type": 0,
        "value": "Location Map"
      }
    ],
    "venueFeatureList.venueSpa": [
      {
        "type": 0,
        "value": "Spa"
      }
    ],
    "venueFeatureList.venueWifi": [
      {
        "type": 0,
        "value": "Wifi"
      }
    ],
    "venueFeaturesList.venueAmenities": [
      {
        "type": 0,
        "value": "Amenities"
      }
    ],
    "venueFeaturesList.venueBeachName": [
      {
        "type": 0,
        "value": "Beach"
      }
    ],
    "venueFeaturesList.venueBookNow": [
      {
        "type": 0,
        "value": "Book Now"
      }
    ],
    "venueFeaturesList.venueBusinessName": [
      {
        "type": 0,
        "value": "Business"
      }
    ],
    "venueFeaturesList.venueFamily": [
      {
        "type": 0,
        "value": "Family"
      }
    ],
    "venueFeaturesList.venueFreeWifi": [
      {
        "type": 0,
        "value": "Free Wifi"
      }
    ],
    "venueFeaturesList.venueGym": [
      {
        "type": 0,
        "value": "Gym"
      }
    ],
    "venueFeaturesList.venueHolistic": [
      {
        "type": 0,
        "value": "Holistic"
      }
    ],
    "venueFeaturesList.venueKidsProgram": [
      {
        "type": 0,
        "value": "Kids Program"
      }
    ],
    "venueFeaturesList.venueMovementFitness": [
      {
        "type": 0,
        "value": "Movement Fitness"
      }
    ],
    "venueFeaturesList.venuePool": [
      {
        "type": 0,
        "value": "Pool"
      }
    ],
    "venueFeaturesList.venueRoomName": [
      {
        "type": 0,
        "value": "Rooms"
      }
    ],
    "venueFeaturesList.venueSki": [
      {
        "type": 0,
        "value": "Ski"
      }
    ],
    "venuePage.proximityNearby": [
      {
        "type": 0,
        "value": "PLACES YOU CAN VISIT"
      }
    ],
    "venuePage.proximityTravel": [
      {
        "type": 0,
        "value": "HOW TO REACH"
      }
    ],
    "venuePage.venueContactName": [
      {
        "type": 0,
        "value": "Contact"
      }
    ]
  },
  "consentEnabled": true,
  "brandIdentityAssets": {
    "favicon": "https://www.wired.com/verso/static/wired-us/assets/favicon.ico",
    "signInModalAsset": {
      "default": {
        "altText": "Sign In",
        "sources": {
          "sm": {
            "url": "/verso/static/wired-us/assets/sign-in-modal.png"
          }
        }
      },
      "crosswords": {
        "altText": "Sign In",
        "sources": {
          "sm": {
            "url": "/verso/static/wired-us/assets/sign-in-modal-crosswords.png"
          }
        }
      },
      "voting": {
        "altText": "Sign In",
        "sources": {
          "sm": {
            "url": "/verso/static/wired-us/assets/sign-in-modal-voting.png"
          }
        }
      }
    }
  },
  "useTrailingSlash": true,
  "globalMessage": null,
  "fingerprint": {
    "isEnabled": true,
    "publicKey": "RnzaPD7aVNbZwmkfojeZ",
    "cookieExpire": 86400000
  },
  "idmapper": {
    "isEnabled": true,
    "publicKey": "eff659437152695c6eda4513907144d0",
    "url": "https://id-mapper-service.gp-prod.conde.digital"
  },
  "crossDomainLinks": [],
  "cytokine": {
    "url": "https://www.wired.com/cytokine/deploy/master/cytokine-7cfd1c225a71fd2ce4b92c32a109919b.js",
    "rotatingUrl": "https://www.wired.com/1cfD83tzv-t6BCE08VW-kwAmc_4uEm_0mTzcSE2Of34-r3D6aVCIAI9O933EbBKO3l03XZl2gOUpXF9-8I9msNDuazj-8OaK5Yqj5t8bO-VkLeAu3q2R87h53S_kY2ryIojrE12RiyQHs",
    "credentials": {
      "id": "verso",
      "key": "H9CMaH7AFkyBTrFteBHIQ1k-dktEty3Y"
    }
  },
  "fastly": {
    "response": {
      "headers": {
        "model-name": "search",
        "modified-at": 1738898804
      }
    }
  },
  "google": {
    "isSwgEnabledOnTenantChannel": true,
    "isSwgEnabledOnSystem": false,
    "registrationSourceCode": "",
    "swgPublicationId": "wired.com",
    "swgSku": "swg_annual_intro_offer",
    "entitlement": {
      "processEntitlementResponse": false
    }
  },
  "head.canonicalUrl": "https://www.wired.com/search/?page=2",
  "head.hreflang": [],
  "head.description": "Search",
  "head.keywords": "",
  "head.og.type": "website",
  "head.robots": "index, follow, noarchive, max-image-preview:large",
  "head.title": "Search | Page 2 | WIRED",
  "tenant": "wired",
  "head.social.title": "Search",
  "head.social.description": "",
  "head.promo.dek": "Search",
  "head.social.opinion": "false",
  "head.pageType": "search",
  "head.primaryTagsRoot": "tags",
  "head.hasSponsoredContent": false,
  "head.modifiedDate": "",
  "head.noIndex": false,
  "linkBannerData": {
    "bannerType": "marquee",
    "dek": "",
    "hed": "",
    "image": {},
    "links": [],
    "tracking": {
      "trackingIdentifier": "",
      "attributes": {}
    }
  },
  "linkBannerId": [],
  "navigation": {
    "aboutText": "WIRED is where tomorrow is realized. It is the essential source of information and ideas that make sense of a world in constant transformation. The WIRED conversation illuminates how technology is changing every aspect of our lives—from culture to business, science to design. The breakthroughs and innovations that we uncover lead to new ways of thinking, new connections, and new industries.",
    "appDownloadUrls": [],
    "account": {
      "signInLink": "/auth/initiate?redirectURL=%2Fsearch%2F&source=VERSO_NAVIGATION",
      "accountLinks": [
        {
          "attributes": {
            "name": "/my-account"
          },
          "index": 0,
          "nodeType": "link",
          "text": "My Account",
          "url": "/account/profile"
        },
        {
          "attributes": {
            "name": "/verify-subscription"
          },
          "index": 1,
          "nodeType": "link",
          "paymentGroup": "subscription-workflow",
          "text": "Verify Subscription",
          "url": "/account/link"
        },
        {
          "attributes": {
            "name": "/view-saved-stories"
          },
          "index": 2,
          "isProfileLink": true,
          "nodeType": "link",
          "text": "View Saved Stories",
          "url": "/account/saved"
        },
        {
          "attributes": {
            "name": "/manage-subscription"
          },
          "index": 3,
          "nodeType": "link",
          "paymentGroup": "subs-cta",
          "text": "Manage subscription",
          "url": "https://subscriptions.wired.com/servlet/RegistrationGateway?cds_mag_code=WIR&cds_config_id=907"
        },
        {
          "attributes": {
            "name": "/sign-out"
          },
          "index": 4,
          "nodeType": "signOut",
          "text": "Sign out",
          "url": "/auth/end?redirectURL=%2Fsearch%2F"
        }
      ],
      "redirectURL": "%2Fsearch%2F"
    },
    "contactLinks": [
      {
        "isExternal": false,
        "text": "Reviews",
        "url": "https://www.wired.com/category/gear/reviews/",
        "isActive": false
      },
      {
        "isExternal": false,
        "text": "Buying Guides",
        "url": "https://www.wired.com/category/gear/buying-guides/",
        "isActive": false
      },
      {
        "isExternal": false,
        "text": "Mattresses",
        "url": "https://www.wired.com/gallery/best-mattresses/",
        "isActive": false
      },
      {
        "isExternal": false,
        "text": "Electric Bikes",
        "url": "https://www.wired.com/gallery/best-electric-bikes/",
        "isActive": false
      },
      {
        "text": "Soundbars",
        "url": "https://www.wired.com/gallery/best-soundbars/",
        "isActive": false
      },
      {
        "text": "Streaming Guides",
        "url": "https://www.wired.com/tag/culture-guides/",
        "isActive": false
      },
      {
        "text": "Wearables",
        "url": "https://www.wired.com/tag/wearables/",
        "isActive": false
      },
      {
        "text": "TVs",
        "url": "https://www.wired.com/gallery/best-tvs/",
        "isActive": false
      },
      {
        "text": "Coupons",
        "url": "https://www.wired.com/tag/coupons/",
        "isActive": false
      },
      {
        "text": "Code Guarantee",
        "url": "https://www.wired.com/coupons/info/code-guarantee.html",
        "isActive": false
      },
      {
        "text": "Gift Guides",
        "url": "/tag/gift-guides/",
        "isActive": false
      }
    ],
    "contactLinksHeading": "Reviews and Guides",
    "footerLinks": [
      {
        "isExternal": false,
        "text": "Subscribe",
        "url": "https://www.wired.com/subscribe/",
        "isActive": false
      },
      {
        "isExternal": false,
        "text": "Newsletters",
        "url": "https://www.wired.com/newsletter?sourceCode=HeaderAndFooter",
        "isActive": false
      },
      {
        "isExternal": false,
        "text": "FAQ",
        "url": "https://www.wired.com/about/faq/",
        "isActive": false
      },
      {
        "isExternal": false,
        "text": "WIRED Staff",
        "url": "https://www.wired.com/about/wired-staff/",
        "isActive": false
      },
      {
        "text": "WIRED Education",
        "url": "https://www.wirededucation.com/",
        "isActive": false
      },
      {
        "text": "Editorial Standards",
        "url": "https://www.wired.com/about/wired-on-background-policy/",
        "isActive": false
      },
      {
        "text": "Archive",
        "url": "https://archive.wired.com/t/storefront/storefront",
        "isActive": false
      },
      {
        "text": "RSS",
        "url": "https://www.wired.com/about/rss-feeds/",
        "isActive": false
      },
      {
        "text": "Accessibility Help",
        "url": "https://www.wired.com/about/accessibility-help/",
        "isActive": false
      }
    ],
    "footerLinksHeading": "More From WIRED",
    "hasChannelNavigation": false,
    "hasSEOSupport": false,
    "internationalInfo": {
      "homeLocation": {
        "name": "United States"
      },
      "internationalSites": [
        {
          "name": "Italia",
          "url": "https://www.wired.it/"
        },
        {
          "name": "Japón",
          "url": "https://wired.jp/"
        },
        {
          "name": "Czech Republic & Slovakia",
          "url": "https://www.wired.cz/"
        }
      ]
    },
    "isEditorPicksAvailable": false,
    "noticesLinks": [
      {
        "text": "Advertise",
        "url": "https://www.condenast.com/brands/wired",
        "isActive": false
      },
      {
        "text": "Contact Us",
        "url": "https://www.wired.com/about/feedback/",
        "isActive": false
      },
      {
        "text": "Manage Account",
        "url": "https://www.wired.com/account/profile",
        "isActive": false
      },
      {
        "text": "Jobs",
        "url": "https://www.wired.com/about/wired-jobs/",
        "isActive": false
      },
      {
        "text": "Press Center",
        "url": "https://www.wired.com/about/press/",
        "isActive": false
      },
      {
        "isExternal": true,
        "text": "Condé Nast Store",
        "url": "https://www.condenaststore.com/",
        "isActive": false
      },
      {
        "isExternal": true,
        "text": "User Agreement",
        "url": "https://www.condenast.com/user-agreement/",
        "rel": "nofollow",
        "isActive": false
      },
      {
        "isExternal": true,
        "text": "Privacy Policy",
        "url": "http://www.condenast.com/privacy-policy#privacypolicy",
        "rel": "nofollow",
        "isActive": false
      },
      {
        "isExternal": true,
        "text": "Your California Privacy Rights",
        "url": "http://www.condenast.com/privacy-policy#privacypolicy-california",
        "rel": "nofollow",
        "isActive": false
      }
    ],
    "primaryLinks": [
      {
        "isExternal": false,
        "showInTopNav": true,
        "text": "Security",
        "url": "/category/security/",
        "forceLeftOfNav": false,
        "isActive": false
      },
      {
        "isExternal": false,
        "showInTopNav": true,
        "text": "Politics",
        "url": "https://www.wired.com/category/politics/",
        "forceLeftOfNav": false,
        "isActive": false
      },
      {
        "isExternal": false,
        "showInTopNav": true,
        "text": "Gear",
        "url": "/category/gear/",
        "forceLeftOfNav": false,
        "isActive": false
      },
      {
        "isExternal": false,
        "showInTopNav": true,
        "text": "The Big Story",
        "url": "/category/big-story/",
        "forceLeftOfNav": false,
        "isActive": false
      },
      {
        "isExternal": false,
        "showInTopNav": true,
        "text": "Business",
        "url": "/category/business/",
        "forceLeftOfNav": false,
        "isActive": false
      },
      {
        "isExternal": false,
        "showInTopNav": true,
        "text": "Science",
        "url": "/category/science/",
        "forceLeftOfNav": false,
        "isActive": false
      },
      {
        "isExternal": false,
        "showInTopNav": true,
        "text": "Culture",
        "url": "/category/culture/",
        "forceLeftOfNav": false,
        "isActive": false
      },
      {
        "isExternal": false,
        "showInTopNav": true,
        "text": "Ideas",
        "url": "/category/ideas/",
        "forceLeftOfNav": false,
        "isActive": false
      },
      {
        "isExternal": true,
        "showInTopNav": true,
        "text": "Merch",
        "url": "https://shop.wired.com/",
        "forceLeftOfNav": false,
        "isActive": false
      }
    ],
    "searchLink": "/search/",
    "secondaryLinks": [
      {
        "isExternal": false,
        "text": "Podcasts",
        "url": "/podcasts/",
        "isActive": false
      },
      {
        "isExternal": false,
        "text": "Video",
        "url": "/video/",
        "isActive": false
      },
      {
        "isExternal": false,
        "text": "Newsletters",
        "url": "https://www.wired.com/newsletter?sourceCode=navbar",
        "isActive": false
      },
      {
        "isExternal": false,
        "text": "Magazine",
        "url": "https://www.wired.com/magazine",
        "isActive": false
      },
      {
        "isExternal": false,
        "text": "Travel",
        "url": "http://wired.com/travel",
        "isActive": false
      },
      {
        "text": "Steven Levy's Plaintext Column",
        "url": "https://www.wired.com/tag/plaintext/",
        "isActive": false
      },
      {
        "text": "WIRED Classics from the Archive",
        "url": "https://www.wired.com/tag/wired-classic/",
        "isActive": false
      },
      {
        "isExternal": false,
        "text": "Events",
        "url": "https://www.wired.com/tag/wired-events/",
        "isActive": false
      },
      {
        "isExternal": false,
        "text": "WIRED Insider",
        "url": "/category/wiredinsider/",
        "isActive": false
      },
      {
        "text": "WIRED Consulting",
        "url": "/tag/wired-consulting/ ",
        "isActive": false
      },
      {
        "isExternal": false,
        "text": "Coupons",
        "url": "https://www.wired.com/coupons",
        "isActive": false
      }
    ],
    "callToActionLink": {
      "url": "",
      "text": "",
      "verboseText": ""
    },
    "pageHeadline": "Search",
    "socialLinks": [
      {
        "label": "Follow us on Facebook",
        "network": "facebook",
        "url": "https://www.facebook.com/wired/"
      },
      {
        "label": "Follow us on X",
        "network": "twitter",
        "url": "https://twitter.com/wired/"
      },
      {
        "label": "Follow us on Pinterest",
        "network": "pinterest",
        "url": "https://pinterest.com/wired/"
      },
      {
        "label": "Follow us on YouTube",
        "network": "youtube",
        "url": "https://www.youtube.com/user/wired/"
      },
      {
        "label": "Follow us on Instagram",
        "network": "instagram",
        "url": "https://instagram.com/wired/"
      },
      {
        "label": "Follow us on TikTok",
        "network": "tiktok",
        "url": "https://www.tiktok.com/@wired?lang=en"
      }
    ],
    "socialLinksHeading": "",
    "subchannelLinks": [],
    "utilityLinks": [
      {
        "cmPosition": "nav-cta",
        "paymentGroup": "consumer-marketing",
        "forceLeftOfNav": false,
        "isActive": false
      },
      {
        "text": "Give a Gift",
        "url": "https://subscribe.wired.com/subscribe/splits/wired/WIR_GIFT?source=WIR_Actives_Gift",
        "forceLeftOfNav": false,
        "showInTopNav": false,
        "isExternal": true,
        "paymentGroup": "subs-cta",
        "isActive": false
      }
    ]
  },
  "isAccountsEnabled": true,
  "accountProps": {
    "signInLink": "/auth/initiate?redirectURL=%2Fsearch%2F&source=VERSO_NAVIGATION",
    "accountLinks": [
      {
        "attributes": {
          "name": "/my-account"
        },
        "index": 0,
        "nodeType": "link",
        "text": "My Account",
        "url": "/account/profile"
      },
      {
        "attributes": {
          "name": "/verify-subscription"
        },
        "index": 1,
        "nodeType": "link",
        "paymentGroup": "subscription-workflow",
        "text": "Verify Subscription",
        "url": "/account/link"
      },
      {
        "attributes": {
          "name": "/view-saved-stories"
        },
        "index": 2,
        "isProfileLink": true,
        "nodeType": "link",
        "text": "View Saved Stories",
        "url": "/account/saved"
      },
      {
        "attributes": {
          "name": "/manage-subscription"
        },
        "index": 3,
        "nodeType": "link",
        "paymentGroup": "subs-cta",
        "text": "Manage subscription",
        "url": "https://subscriptions.wired.com/servlet/RegistrationGateway?cds_mag_code=WIR&cds_config_id=907"
      },
      {
        "attributes": {
          "name": "/sign-out"
        },
        "index": 4,
        "nodeType": "signOut",
        "text": "Sign out",
        "url": "/auth/end?redirectURL=%2Fsearch%2F"
      }
    ],
    "redirectURL": "%2Fsearch%2F"
  },
  "parsely": {
    "isEnabled": false,
    "publicKey": "",
    "shouldRenderParsely": true
  },
  "sentry": {
    "dsn": ""
  },
  "shopifyConfiguration": {},
  "appConfig": {
    "brandSlug": "wired"
  },
  "userPlatform": {
    "isDomainSigninSwitchEnabled": false,
    "siteCode": "WIR",
    "userPlatformProxy": "https://www.wired.com/api/up",
    "xClientID": "Verso-Wired",
    "filterBookmarkTypes": [],
    "federatedGraphqlUrl": "https://graphql.condenast.io/graphql"
  },
  "experiments": {
    "assignments": []
  },
  "martechPlatform": {
    "isEnabled": true,
    "products": [
      "wired:web:basic"
    ],
    "redirectURL": "/",
    "isAccessCookieEnabled": true
  },
  "admiral": {
    "enabled": true,
    "bundle": "!(function(o,_name){o[_name]=o[_name]||function $(){($.q=$.q||[]).push(arguments)},o[_name].v=o[_name].v||2,o[_name].s=\"3\";!(function(o,t,e,n,c,a,f){function i(n,c){(n=(function(t,e){try{if(e=(t=o.localStorage).getItem(\"_aQS01Q0IwOTY5NTEzOUM2MDU3MEU5M0VGREEtMTk\"))return JSON.parse(e).lgk||[];if((f=t.getItem(decodeURI(decodeURI('%25%37%364ac%31e%69%25%35a%257%320'))))&&f.split(\",\")[4]>0)return[[_name+\"-engaged\",\"true\"]]}catch(n){}})())&&typeof n.forEach===e&&(c=o[t].pubads())&&n.forEach((function(o){o&&o[0]&&c.setTargeting(o[0],o[1]||\"\")}))}try{(a=o[t]=o[t]||{}).cmd=a.cmd||[],typeof a.pubads===e?i():typeof a.cmd.unshift===e?a.cmd.unshift(i):a.cmd.push(i)}catch(r){}})(window,\"googletag\",\"function\");;})(window,decodeURI(decodeURI('%61%256%34mi%25%372%25%361%25%36c')));!(function(t,c,o,$){o=t.createElement(c),t=t.getElementsByTagName(c)[0],o.async=1,o.src=\"https://pricklypollution.com/j/3c3d4edf5/28d5b6b532b3d09c2b6b47d6fb573752df6c9-prod.js\",($=0)&&$(o),t.parentNode.insertBefore(o,t)})(document,\"script\");"
  },
  "search": {
    "brandName": "WIRED",
    "buttonType": "more",
    "contentTitle": "Results",
    "contentType": "",
    "currentPage": 2,
    "hasGrid": false,
    "isEmptyQuery": true,
    "items": [
      {
        "id": "67a0e2229a0b76568e4f0fb5",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/matt-reynolds/\">Matt Reynolds</a> is a senior writer at WIRED, where he covers climate, food, and biodiversity. Before that he was a technology journalist at New Scientist magazine. His first book, <em>The Future of Food: How to Feed the Planet Without Destroying It</em>, was published in 2021. Reynolds is a graduate of ... <a href=\"/author/matt-reynolds\">Read more</a>",
                "dangerousTitle": "Senior writer",
                "name": "Matt Reynolds",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "mattsreynolds1",
                    "network": "twitter",
                    "label": "Follow Matt Reynolds on X"
                  }
                ],
                "url": "/author/matt-reynolds/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "67a0e2229a0b76568e4f0fb5",
        "dangerousHed": "This Weird, Fleshy Novel Is Exactly What You Need Right Now",
        "dangerousDek": "<em>Dengue Boy</em>, a book about a humanoid mosquito taking his revenge in the dying years of planet Earth, is unsettling and essential.",
        "date": "02.05.2025",
        "pubDate": "2025-02-05T18:12:54.656Z",
        "issueDate": "",
        "image": {
          "altText": "Search",
          "caption": "",
          "contentType": "photo",
          "credit": "Photo-Illustration: Wired Staff/Getty Images",
          "id": "67a26174a30fe8e58cb48fb4",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_1024,c_limit/mosquito-mutant-sci.jpg",
              "srcset": "https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_120,c_limit/mosquito-mutant-sci.jpg 120w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_240,c_limit/mosquito-mutant-sci.jpg 240w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_320,c_limit/mosquito-mutant-sci.jpg 320w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_640,c_limit/mosquito-mutant-sci.jpg 640w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_960,c_limit/mosquito-mutant-sci.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_1280,c_limit/mosquito-mutant-sci.jpg",
              "srcset": "https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_120,c_limit/mosquito-mutant-sci.jpg 120w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_240,c_limit/mosquito-mutant-sci.jpg 240w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_320,c_limit/mosquito-mutant-sci.jpg 320w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_640,c_limit/mosquito-mutant-sci.jpg 640w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_960,c_limit/mosquito-mutant-sci.jpg 960w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_1280,c_limit/mosquito-mutant-sci.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_1280,c_limit/mosquito-mutant-sci.jpg",
              "srcset": "https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_120,c_limit/mosquito-mutant-sci.jpg 120w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_240,c_limit/mosquito-mutant-sci.jpg 240w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_320,c_limit/mosquito-mutant-sci.jpg 320w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_640,c_limit/mosquito-mutant-sci.jpg 640w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_960,c_limit/mosquito-mutant-sci.jpg 960w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_1280,c_limit/mosquito-mutant-sci.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_1024,c_limit/mosquito-mutant-sci.jpg",
              "srcset": "https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_120,c_limit/mosquito-mutant-sci.jpg 120w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_240,c_limit/mosquito-mutant-sci.jpg 240w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_320,c_limit/mosquito-mutant-sci.jpg 320w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_640,c_limit/mosquito-mutant-sci.jpg 640w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_960,c_limit/mosquito-mutant-sci.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_1280,c_limit/mosquito-mutant-sci.jpg",
              "srcset": "https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_120,c_limit/mosquito-mutant-sci.jpg 120w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_240,c_limit/mosquito-mutant-sci.jpg 240w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_320,c_limit/mosquito-mutant-sci.jpg 320w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_640,c_limit/mosquito-mutant-sci.jpg 640w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_960,c_limit/mosquito-mutant-sci.jpg 960w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_1280,c_limit/mosquito-mutant-sci.jpg 1280w"
            }
          },
          "masterAspectRatio": "2400:2400",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_1024,c_limit/mosquito-mutant-sci.jpg",
                "srcset": "https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_120,c_limit/mosquito-mutant-sci.jpg 120w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_240,c_limit/mosquito-mutant-sci.jpg 240w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_320,c_limit/mosquito-mutant-sci.jpg 320w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_640,c_limit/mosquito-mutant-sci.jpg 640w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/16:9/w_960,c_limit/mosquito-mutant-sci.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_1280,c_limit/mosquito-mutant-sci.jpg",
                "srcset": "https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_120,c_limit/mosquito-mutant-sci.jpg 120w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_240,c_limit/mosquito-mutant-sci.jpg 240w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_320,c_limit/mosquito-mutant-sci.jpg 320w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_640,c_limit/mosquito-mutant-sci.jpg 640w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_960,c_limit/mosquito-mutant-sci.jpg 960w, https://media.wired.com/photos/67a26174a30fe8e58cb48fb4/3:2/w_1280,c_limit/mosquito-mutant-sci.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Buzz Off"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "This Weird, Fleshy Novel Is Exactly What You Need Right Now",
          "dek": "*Dengue Boy*, a book about a humanoid mosquito taking his revenge in the dying years of planet Earth, is unsettling and essential."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/this-weird-fleshy-novel-is-exactly-what-you-need-right-now-dengue-boy-michael-nieva/",
        "functionalTags": []
      },
      {
        "id": "67a2e37506a055adc4e3d3d7",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/matt-burgess/\">Matt Burgess</a> is a senior writer at WIRED focused on information security, privacy, and data regulation in Europe. He graduated from the University of Sheffield with a degree in journalism and now lives in London. Send tips to Matt_Burgess@wired.com. ... <a href=\"/author/matt-burgess\">Read more</a>",
                "dangerousTitle": "Senior writer",
                "name": "Matt Burgess",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e713244d9f150f523145c2/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e713244d9f150f523145c2/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "mattburgess1",
                    "network": "twitter",
                    "label": "Follow Matt Burgess on X"
                  }
                ],
                "url": "/author/matt-burgess/"
              },
              {
                "dangerousBio": "<a href=\"/author/lily-hay-newman/\">Lily Hay Newman</a> is a senior writer at WIRED focused on information security, digital privacy, and hacking. She previously worked as a technology reporter at Slate, and was the staff writer for Future Tense, a publication and partnership between Slate, the New America Foundation, and Arizona State University. Her work ... <a href=\"/author/lily-hay-newman\">Read more</a>",
                "dangerousTitle": "Senior Writer",
                "name": "Lily Hay Newman",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "lilyhnewman",
                    "network": "twitter",
                    "label": "Follow Lily Hay Newman on X"
                  }
                ],
                "url": "/author/lily-hay-newman/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "67a2e37506a055adc4e3d3d7",
        "dangerousHed": "The Collapse of USAID Is Already Fueling Human Trafficking and Slavery at Scammer Compounds",
        "dangerousDek": "The dismantling of USAID by Elon Musk&#39;s DOGE and a State Department funding freeze have severely disrupted efforts to help people escape forced labor camps run by criminal scammers.",
        "date": "02.05.2025",
        "pubDate": "2025-02-05T17:33:53.551Z",
        "issueDate": "",
        "image": {
          "altText": "people protesting outside the US Agency for International Development holding signs saying SAVE USAID SAVE LIVES",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Kayla Bartkowski/Getty Images",
          "id": "67a3883d049ed233afcda9b2",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_1024,c_limit/usaid-sec-2197486320.jpg",
              "srcset": "https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_120,c_limit/usaid-sec-2197486320.jpg 120w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_240,c_limit/usaid-sec-2197486320.jpg 240w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_320,c_limit/usaid-sec-2197486320.jpg 320w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_640,c_limit/usaid-sec-2197486320.jpg 640w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_960,c_limit/usaid-sec-2197486320.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_1280,c_limit/usaid-sec-2197486320.jpg",
              "srcset": "https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_120,c_limit/usaid-sec-2197486320.jpg 120w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_240,c_limit/usaid-sec-2197486320.jpg 240w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_320,c_limit/usaid-sec-2197486320.jpg 320w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_640,c_limit/usaid-sec-2197486320.jpg 640w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_960,c_limit/usaid-sec-2197486320.jpg 960w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_1280,c_limit/usaid-sec-2197486320.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_1280,c_limit/usaid-sec-2197486320.jpg",
              "srcset": "https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_120,c_limit/usaid-sec-2197486320.jpg 120w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_240,c_limit/usaid-sec-2197486320.jpg 240w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_320,c_limit/usaid-sec-2197486320.jpg 320w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_640,c_limit/usaid-sec-2197486320.jpg 640w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_960,c_limit/usaid-sec-2197486320.jpg 960w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_1280,c_limit/usaid-sec-2197486320.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_1024,c_limit/usaid-sec-2197486320.jpg",
              "srcset": "https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_120,c_limit/usaid-sec-2197486320.jpg 120w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_240,c_limit/usaid-sec-2197486320.jpg 240w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_320,c_limit/usaid-sec-2197486320.jpg 320w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_640,c_limit/usaid-sec-2197486320.jpg 640w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_960,c_limit/usaid-sec-2197486320.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_1280,c_limit/usaid-sec-2197486320.jpg",
              "srcset": "https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_120,c_limit/usaid-sec-2197486320.jpg 120w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_240,c_limit/usaid-sec-2197486320.jpg 240w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_320,c_limit/usaid-sec-2197486320.jpg 320w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_640,c_limit/usaid-sec-2197486320.jpg 640w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_960,c_limit/usaid-sec-2197486320.jpg 960w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_1280,c_limit/usaid-sec-2197486320.jpg 1280w"
            }
          },
          "masterAspectRatio": "2400:2400",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_1024,c_limit/usaid-sec-2197486320.jpg",
                "srcset": "https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_120,c_limit/usaid-sec-2197486320.jpg 120w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_240,c_limit/usaid-sec-2197486320.jpg 240w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_320,c_limit/usaid-sec-2197486320.jpg 320w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_640,c_limit/usaid-sec-2197486320.jpg 640w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/16:9/w_960,c_limit/usaid-sec-2197486320.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_1280,c_limit/usaid-sec-2197486320.jpg",
                "srcset": "https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_120,c_limit/usaid-sec-2197486320.jpg 120w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_240,c_limit/usaid-sec-2197486320.jpg 240w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_320,c_limit/usaid-sec-2197486320.jpg 320w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_640,c_limit/usaid-sec-2197486320.jpg 640w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_960,c_limit/usaid-sec-2197486320.jpg 960w, https://media.wired.com/photos/67a3883d049ed233afcda9b2/3:2/w_1280,c_limit/usaid-sec-2197486320.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Rug Pull"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "The Collapse of USAID Is Already Fueling Human Trafficking and Slavery at Scammer Compounds",
          "dek": "The dismantling of USAID by Elon Musk’s DOGE and a State Department funding freeze have severely disrupted efforts to help people escape forced labor camps run by criminal scammers."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/usaid-collapse-is-helping-criminal-scammers-enslave-people/",
        "functionalTags": []
      },
      {
        "id": "67a2438f672b0385ed7ca0be",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/david-gilbert/\">David Gilbert</a> is a reporter at WIRED covering disinformation, online extremism, and how these two online trends impact people’s lives across the globe, with a special focus on the 2024 US presidential election. Prior to joining WIRED, he worked at VICE News. He lives in Ireland. ... <a href=\"/author/david-gilbert\">Read more</a>",
                "dangerousTitle": "Reporter",
                "name": "David Gilbert",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/663a737bf79ecb6f05993e53/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "daithaigilbert",
                    "network": "twitter",
                    "label": "Follow David Gilbert on X"
                  }
                ],
                "url": "/author/david-gilbert/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "67a2438f672b0385ed7ca0be",
        "dangerousHed": "The Far Right Has a New Hero: Elon Musk",
        "dangerousDek": "Elon Musk’s takeover of the federal government has inspired adoration from far-right communities online that used to be reserved for Donald Trump.",
        "date": "02.05.2025",
        "pubDate": "2025-02-05T17:11:39.797Z",
        "issueDate": "",
        "image": {
          "altText": "Search",
          "caption": "",
          "contentType": "photo",
          "credit": "Photo-Illustration: Wired Staff; Ying Tang/Getty Images",
          "id": "67a24e7d0a98743a8c788fff",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_1024,c_limit/musk-nazi-pol-%202195229169.jpg",
              "srcset": "https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_120,c_limit/musk-nazi-pol-%202195229169.jpg 120w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_240,c_limit/musk-nazi-pol-%202195229169.jpg 240w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_320,c_limit/musk-nazi-pol-%202195229169.jpg 320w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_640,c_limit/musk-nazi-pol-%202195229169.jpg 640w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_960,c_limit/musk-nazi-pol-%202195229169.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_1280,c_limit/musk-nazi-pol-%202195229169.jpg",
              "srcset": "https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_120,c_limit/musk-nazi-pol-%202195229169.jpg 120w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_240,c_limit/musk-nazi-pol-%202195229169.jpg 240w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_320,c_limit/musk-nazi-pol-%202195229169.jpg 320w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_640,c_limit/musk-nazi-pol-%202195229169.jpg 640w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_960,c_limit/musk-nazi-pol-%202195229169.jpg 960w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_1280,c_limit/musk-nazi-pol-%202195229169.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_1280,c_limit/musk-nazi-pol-%202195229169.jpg",
              "srcset": "https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_120,c_limit/musk-nazi-pol-%202195229169.jpg 120w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_240,c_limit/musk-nazi-pol-%202195229169.jpg 240w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_320,c_limit/musk-nazi-pol-%202195229169.jpg 320w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_640,c_limit/musk-nazi-pol-%202195229169.jpg 640w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_960,c_limit/musk-nazi-pol-%202195229169.jpg 960w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_1280,c_limit/musk-nazi-pol-%202195229169.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_1024,c_limit/musk-nazi-pol-%202195229169.jpg",
              "srcset": "https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_120,c_limit/musk-nazi-pol-%202195229169.jpg 120w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_240,c_limit/musk-nazi-pol-%202195229169.jpg 240w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_320,c_limit/musk-nazi-pol-%202195229169.jpg 320w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_640,c_limit/musk-nazi-pol-%202195229169.jpg 640w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_960,c_limit/musk-nazi-pol-%202195229169.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_1280,c_limit/musk-nazi-pol-%202195229169.jpg",
              "srcset": "https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_120,c_limit/musk-nazi-pol-%202195229169.jpg 120w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_240,c_limit/musk-nazi-pol-%202195229169.jpg 240w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_320,c_limit/musk-nazi-pol-%202195229169.jpg 320w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_640,c_limit/musk-nazi-pol-%202195229169.jpg 640w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_960,c_limit/musk-nazi-pol-%202195229169.jpg 960w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_1280,c_limit/musk-nazi-pol-%202195229169.jpg 1280w"
            }
          },
          "masterAspectRatio": "2400:2400",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_1024,c_limit/musk-nazi-pol-%202195229169.jpg",
                "srcset": "https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_120,c_limit/musk-nazi-pol-%202195229169.jpg 120w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_240,c_limit/musk-nazi-pol-%202195229169.jpg 240w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_320,c_limit/musk-nazi-pol-%202195229169.jpg 320w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_640,c_limit/musk-nazi-pol-%202195229169.jpg 640w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/16:9/w_960,c_limit/musk-nazi-pol-%202195229169.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_1280,c_limit/musk-nazi-pol-%202195229169.jpg",
                "srcset": "https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_120,c_limit/musk-nazi-pol-%202195229169.jpg 120w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_240,c_limit/musk-nazi-pol-%202195229169.jpg 240w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_320,c_limit/musk-nazi-pol-%202195229169.jpg 320w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_640,c_limit/musk-nazi-pol-%202195229169.jpg 640w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_960,c_limit/musk-nazi-pol-%202195229169.jpg 960w, https://media.wired.com/photos/67a24e7d0a98743a8c788fff/3:2/w_1280,c_limit/musk-nazi-pol-%202195229169.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Takeover"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "The Far Right Has a New Hero: Elon Musk",
          "dek": "Elon Musk’s takeover of the federal government has inspired adoration from far-right communities online that used to be reserved for Donald Trump."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/far-right-new-leader-elon-musk/",
        "functionalTags": []
      },
      {
        "id": "67a131d34f0b06eb394294e4",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/will-knight/\">Will Knight</a> is a senior writer for WIRED, covering artificial intelligence. He writes the <a href=\"https://www.wired.com/newsletter/ai-lab?sourceCode=AuthorBio\"><em>AI Lab</em> newsletter</a>, a weekly dispatch from beyond the cutting edge of AI&#8212;<a href=\"https://www.wired.com/newsletter/ai-lab?sourceCode=AuthorBio\"><strong>sign up here</strong></a>. He was previously a senior editor at MIT Technology Review, where he wrote about fundamental advances in AI and China’s AI ... <a href=\"/author/will-knight\">Read more</a>",
                "dangerousTitle": "Senior Writer",
                "name": "Will Knight",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05bc0c761e833be17fee/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b05bc0c761e833be17fee/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "willknight",
                    "network": "twitter",
                    "label": "Follow Will Knight on X"
                  }
                ],
                "url": "/author/will-knight/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "67a131d34f0b06eb394294e4",
        "dangerousHed": "LinkedIn Is Testing an AI Tool That Could Transform How People Search for Jobs",
        "dangerousDek": "The company says artificial intelligence could help surface jobs that remain hidden from typical search queries.",
        "date": "02.05.2025",
        "pubDate": "2025-02-05T17:00:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "A photo illustration of a man searching for work in the classifieds section of the newspaper juxtaposed behind puzzle...",
          "caption": "",
          "contentType": "photo",
          "credit": "Photo-Illustration: WIRED Staff/Getty Images",
          "id": "67a291d3347f6f06d2a353a0",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_1024,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg",
              "srcset": "https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_120,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 120w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_240,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 240w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_320,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 320w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_640,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 640w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_960,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_1280,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg",
              "srcset": "https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_120,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 120w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_240,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 240w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_320,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 320w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_640,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 640w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_960,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 960w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_1280,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_1280,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg",
              "srcset": "https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_120,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 120w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_240,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 240w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_320,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 320w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_640,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 640w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_960,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 960w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_1280,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_1024,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg",
              "srcset": "https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_120,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 120w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_240,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 240w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_320,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 320w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_640,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 640w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_960,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_1280,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg",
              "srcset": "https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_120,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 120w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_240,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 240w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_320,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 320w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_640,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 640w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_960,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 960w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_1280,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 1280w"
            }
          },
          "masterAspectRatio": "2000:2000",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_1024,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg",
                "srcset": "https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_120,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 120w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_240,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 240w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_320,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 320w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_640,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 640w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/16:9/w_960,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_1280,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg",
                "srcset": "https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_120,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 120w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_240,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 240w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_320,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 320w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_640,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 640w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_960,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 960w, https://media.wired.com/photos/67a291d3347f6f06d2a353a0/3:2/w_1280,c_limit/AI-Lab-LinkedIn-LLM-Job-Search-Business-94944500.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "AI Lab"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "LinkedIn Is Testing an AI Tool That Could Transform How People Search for Jobs",
          "dek": "The company says artificial intelligence could help surface jobs that remain hidden from typical search queries."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/linkedin-job-search-artificial-intelligence/",
        "functionalTags": []
      },
      {
        "id": "66b3bc2dcddf6b2f9d833413",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/kat-merck/\">Kat Merck</a> is a senior commerce editor for WIRED, where she covers bird feeders, fans, hair straighteners, and everything home-related. An editor and writer for more than 25 years, she has a bachelor’s degree in journalism from California Polytechnic State University, San Luis Obispo. Following stints as associate editor at ... <a href=\"/author/kat-merck\">Read more</a>",
                "dangerousTitle": "Senior Commerce Editor",
                "name": "Kat Merck",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/66942ee0d966f9f0264e0408/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "https://www.linkedin.com/in/kat-merck/",
                    "network": "linkedin",
                    "label": "Follow Kat Merck on LinkedIn"
                  },
                  {
                    "handle": "https://muckrack.com/kat-merck",
                    "network": "website",
                    "label": "Follow Kat Merck on Website"
                  }
                ],
                "url": "/author/kat-merck/"
              }
            ]
          }
        },
        "contentType": "gallery",
        "copilotID": "66b3bc2dcddf6b2f9d833413",
        "dangerousHed": "The Best Fans for Every Use",
        "dangerousDek": "From tower and pedestal styles to utilitarian box fans, these are our WIRED-tested favorites.",
        "date": "02.05.2025",
        "pubDate": "2025-02-05T15:02:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "A variety of electric house fans sitting on a carpeted floor. Decorative background pink and white tiles.",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Kat Merck; Getty Images",
          "id": "67a27b544d22273769c800d0",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_1024,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg",
              "srcset": "https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_120,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 120w, https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_240,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 240w, https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_320,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 320w, https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_640,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 640w, https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_960,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_1280,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg",
              "srcset": "https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_120,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 120w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_240,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 240w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_320,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 320w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_640,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 640w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_960,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 960w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_1280,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_1280,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg",
              "srcset": "https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_120,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 120w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_240,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 240w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_320,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 320w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_640,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 640w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_960,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 960w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_1280,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_1024,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg",
              "srcset": "https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_120,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 120w, https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_240,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 240w, https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_320,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 320w, https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_640,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 640w, https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_960,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_1280,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg",
              "srcset": "https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_120,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 120w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_240,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 240w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_320,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 320w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_640,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 640w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_960,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 960w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_1280,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 1280w"
            }
          },
          "masterAspectRatio": "2400:1800",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_1024,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg",
                "srcset": "https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_120,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 120w, https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_240,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 240w, https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_320,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 320w, https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_640,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 640w, https://media.wired.com/photos/67a27b544d22273769c800d0/16:9/w_960,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_1280,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg",
                "srcset": "https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_120,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 120w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_240,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 240w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_320,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 320w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_640,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 640w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_960,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 960w, https://media.wired.com/photos/67a27b544d22273769c800d0/3:2/w_1280,c_limit/Best%20Fans%20Reviewer%20Collage%20022025%20SOURCE%20Kat%20Merck.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "itemsCount": {
          "count": 8,
          "itemType": "slide"
        },
        "rubric": {
          "name": "Buying Guide"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "The Best Fans for Every Use",
          "dek": "From tower and pedestal styles to utilitarian box fans, these are our WIRED-tested favorites."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/gallery/best-fans/",
        "functionalTags": []
      },
      {
        "id": "643fb7b378b1686b7e2ea17e",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/simon-hill/\">Simon Hill</a> has been testing and writing about tech for more than 15 years. He is a senior writer for WIRED. You can find his previous work at <em>Business Insider</em>, <em>Reviewed</em>, <em>TechRadar</em>, <em>Android Authority</em>, <em>USA Today</em>, <em>Digital Trends</em>, and many other places. He loves all things tech, but especially smartphones, ... <a href=\"/author/simon-hill\">Read more</a>",
                "dangerousTitle": "Senior Writer and Reviewer",
                "name": "Simon Hill",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05b2721498963daf9aae/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b05b2721498963daf9aae/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "IamSimonHill",
                    "network": "twitter",
                    "label": "Follow Simon Hill on X"
                  },
                  {
                    "handle": "https://www.linkedin.com/in/setimerenptah/",
                    "network": "linkedin",
                    "label": "Follow Simon Hill on LinkedIn"
                  }
                ],
                "url": "/author/simon-hill/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "643fb7b378b1686b7e2ea17e",
        "dangerousHed": "How to Responsibly Dispose of Your Electronics",
        "dangerousDek": "Get rid of old, broken, and unused devices&#8212;even Lightning cables&#8212;without adding to the e-waste problem.",
        "date": "02.05.2025",
        "pubDate": "2025-02-05T14:30:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "Vintage camera with the lens detached from the camera body",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Daniel Grizelj/Getty Images",
          "id": "6442ca70c30f50376ee87348",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_1024,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg",
              "srcset": "https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_120,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 120w, https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_240,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 240w, https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_320,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 320w, https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_640,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 640w, https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_960,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_1280,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg",
              "srcset": "https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_120,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 120w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_240,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 240w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_320,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 320w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_640,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 640w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_960,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 960w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_1280,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_1280,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg",
              "srcset": "https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_120,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 120w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_240,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 240w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_320,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 320w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_640,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 640w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_960,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 960w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_1280,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_1024,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg",
              "srcset": "https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_120,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 120w, https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_240,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 240w, https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_320,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 320w, https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_640,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 640w, https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_960,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_1280,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg",
              "srcset": "https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_120,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 120w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_240,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 240w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_320,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 320w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_640,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 640w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_960,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 960w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_1280,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 1280w"
            }
          },
          "masterAspectRatio": "2400:1800",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_1024,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg",
                "srcset": "https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_120,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 120w, https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_240,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 240w, https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_320,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 320w, https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_640,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 640w, https://media.wired.com/photos/6442ca70c30f50376ee87348/16:9/w_960,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_1280,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg",
                "srcset": "https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_120,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 120w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_240,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 240w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_320,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 320w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_640,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 640w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_960,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 960w, https://media.wired.com/photos/6442ca70c30f50376ee87348/3:2/w_1280,c_limit/How-to-Responsibly-Dispose-of-Your-Electronics-Gear-GettyImages-106421334.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Please Recycle"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "How to Responsibly Dispose of Your Electronics",
          "dek": "Get rid of old, broken, and unused devices—even Lightning cables—without adding to the e-waste problem."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/how-to-responsibly-dispose-electronics/",
        "functionalTags": []
      },
      {
        "id": "677f466fef2790b4178b5fcf",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/boutayna-chokrane/\">Boutayna Chokrane </a>is a product writer and reviewer at WIRED. Before joining the Gear team, she was a music editorial fellow at Pitchfork. She also worked as a freelance journalist, covering fashion, art, and culture for Vogue, Rolling Stone, the Cut, and others. She graduated from Northwestern University with a ... <a href=\"/author/boutayna-chokrane\">Read more</a>",
                "dangerousTitle": "Product Writer &amp; Reviewer",
                "name": "Boutayna Chokrane ",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [],
                "url": "/author/boutayna-chokrane/"
              }
            ]
          }
        },
        "contentType": "review",
        "copilotID": "677f466fef2790b4178b5fcf",
        "dangerousHed": "The Therabody PowerDot 2.0 Duo Really Works, When It Works",
        "dangerousDek": "Therabody’s at-home muscle stimulator is brilliant in theory but is plagued with connectivity issues.",
        "date": "02.05.2025",
        "pubDate": "2025-02-05T14:02:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "Therabody PowerDot 2.0 Duo the nodes and wires of an athome muscle stimulator beside a mobile phone",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Amazon; Getty Images",
          "id": "67a2851810116c4c74647b14",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_1024,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg",
              "srcset": "https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_120,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 120w, https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_240,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 240w, https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_320,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 320w, https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_640,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 640w, https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_960,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_1280,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg",
              "srcset": "https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_120,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 120w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_240,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 240w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_320,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 320w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_640,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 640w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_960,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 960w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_1280,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_1280,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg",
              "srcset": "https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_120,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 120w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_240,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 240w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_320,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 320w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_640,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 640w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_960,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 960w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_1280,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_1024,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg",
              "srcset": "https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_120,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 120w, https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_240,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 240w, https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_320,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 320w, https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_640,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 640w, https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_960,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_1280,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg",
              "srcset": "https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_120,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 120w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_240,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 240w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_320,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 320w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_640,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 640w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_960,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 960w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_1280,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 1280w"
            }
          },
          "masterAspectRatio": "2000:1300",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_1024,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg",
                "srcset": "https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_120,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 120w, https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_240,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 240w, https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_320,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 320w, https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_640,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 640w, https://media.wired.com/photos/67a2851810116c4c74647b14/16:9/w_960,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_1280,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg",
                "srcset": "https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_120,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 120w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_240,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 240w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_320,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 320w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_640,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 640w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_960,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 960w, https://media.wired.com/photos/67a2851810116c4c74647b14/3:2/w_1280,c_limit/Therabody%20PowerDot%202.0%20Duo%20Abstract%20Background%20022025%20SOURCE%20Amazon.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Product Review"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "Review: Therabody PowerDot 2.0 Duo",
          "dek": "Therabody’s at-home muscle stimulator is brilliant in theory but is plagued with connectivity issues."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/review/therabody-powerdot-20-duo/",
        "functionalTags": []
      },
      {
        "id": "679d2ef1d2c9a52a3bce9593",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/andy-greenberg/\">Andy Greenberg</a> is a senior writer for WIRED covering hacking, cybersecurity, and surveillance. He’s the author of the books <em>Tracers in the Dark: The Global Hunt for the Crime Lords of Cryptocurrency</em> and <em>Sandworm: A New Era of Cyberwar and the Hunt for the Kremlin&#39;s Most Dangerous Hackers</em>. His books ... <a href=\"/author/andy-greenberg\">Read more</a>",
                "dangerousTitle": "Senior Writer",
                "name": "Andy Greenberg",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "a_greenberg",
                    "network": "twitter",
                    "label": "Follow Andy Greenberg on X"
                  }
                ],
                "url": "/author/andy-greenberg/"
              },
              {
                "dangerousBio": "<a href=\"/author/lily-hay-newman/\">Lily Hay Newman</a> is a senior writer at WIRED focused on information security, digital privacy, and hacking. She previously worked as a technology reporter at Slate, and was the staff writer for Future Tense, a publication and partnership between Slate, the New America Foundation, and Arizona State University. Her work ... <a href=\"/author/lily-hay-newman\">Read more</a>",
                "dangerousTitle": "Senior Writer",
                "name": "Lily Hay Newman",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e835799fa4c1a0001881a9/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "lilyhnewman",
                    "network": "twitter",
                    "label": "Follow Lily Hay Newman on X"
                  }
                ],
                "url": "/author/lily-hay-newman/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "679d2ef1d2c9a52a3bce9593",
        "dangerousHed": "Despite Catastrophic Hacks, Ransomware Payments Dropped Dramatically Last Year",
        "dangerousDek": "Ransomware gangs continued to wreak havoc in 2024, but new research shows that the amounts victims paid these cybercriminals fell by hundreds of millions of dollars.",
        "date": "02.05.2025",
        "pubDate": "2025-02-05T13:00:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "Search",
          "caption": "",
          "contentType": "photo",
          "credit": "Photo-Illustration: Wired Staff/Getty Images",
          "id": "679d47aed9264dcf927e2847",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_1024,c_limit/crypto-randomware-sec.jpg",
              "srcset": "https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_120,c_limit/crypto-randomware-sec.jpg 120w, https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_240,c_limit/crypto-randomware-sec.jpg 240w, https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_320,c_limit/crypto-randomware-sec.jpg 320w, https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_640,c_limit/crypto-randomware-sec.jpg 640w, https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_960,c_limit/crypto-randomware-sec.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_1280,c_limit/crypto-randomware-sec.jpg",
              "srcset": "https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_120,c_limit/crypto-randomware-sec.jpg 120w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_240,c_limit/crypto-randomware-sec.jpg 240w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_320,c_limit/crypto-randomware-sec.jpg 320w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_640,c_limit/crypto-randomware-sec.jpg 640w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_960,c_limit/crypto-randomware-sec.jpg 960w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_1280,c_limit/crypto-randomware-sec.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_1280,c_limit/crypto-randomware-sec.jpg",
              "srcset": "https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_120,c_limit/crypto-randomware-sec.jpg 120w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_240,c_limit/crypto-randomware-sec.jpg 240w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_320,c_limit/crypto-randomware-sec.jpg 320w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_640,c_limit/crypto-randomware-sec.jpg 640w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_960,c_limit/crypto-randomware-sec.jpg 960w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_1280,c_limit/crypto-randomware-sec.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_1024,c_limit/crypto-randomware-sec.jpg",
              "srcset": "https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_120,c_limit/crypto-randomware-sec.jpg 120w, https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_240,c_limit/crypto-randomware-sec.jpg 240w, https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_320,c_limit/crypto-randomware-sec.jpg 320w, https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_640,c_limit/crypto-randomware-sec.jpg 640w, https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_960,c_limit/crypto-randomware-sec.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_1280,c_limit/crypto-randomware-sec.jpg",
              "srcset": "https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_120,c_limit/crypto-randomware-sec.jpg 120w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_240,c_limit/crypto-randomware-sec.jpg 240w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_320,c_limit/crypto-randomware-sec.jpg 320w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_640,c_limit/crypto-randomware-sec.jpg 640w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_960,c_limit/crypto-randomware-sec.jpg 960w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_1280,c_limit/crypto-randomware-sec.jpg 1280w"
            }
          },
          "masterAspectRatio": "2400:1350",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_1024,c_limit/crypto-randomware-sec.jpg",
                "srcset": "https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_120,c_limit/crypto-randomware-sec.jpg 120w, https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_240,c_limit/crypto-randomware-sec.jpg 240w, https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_320,c_limit/crypto-randomware-sec.jpg 320w, https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_640,c_limit/crypto-randomware-sec.jpg 640w, https://media.wired.com/photos/679d47aed9264dcf927e2847/16:9/w_960,c_limit/crypto-randomware-sec.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_1280,c_limit/crypto-randomware-sec.jpg",
                "srcset": "https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_120,c_limit/crypto-randomware-sec.jpg 120w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_240,c_limit/crypto-randomware-sec.jpg 240w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_320,c_limit/crypto-randomware-sec.jpg 320w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_640,c_limit/crypto-randomware-sec.jpg 640w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_960,c_limit/crypto-randomware-sec.jpg 960w, https://media.wired.com/photos/679d47aed9264dcf927e2847/3:2/w_1280,c_limit/crypto-randomware-sec.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Downward Spiral"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "Despite Catastrophic Hacks, Ransomware Payments Dropped Dramatically Last Year",
          "dek": "Ransomware gangs continued to wreak havoc in 2024, but new research shows that the amounts victims paid these cybercriminals fell by hundreds of millions of dollars."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/2024-ransomware-payments-fall-chainalysis/",
        "functionalTags": []
      },
      {
        "id": "679a4ca2a944607be37796fe",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/louryn-strampe/\">Louryn Strampe</a> is a product writer and reviewer at WIRED covering a little bit of everything. She especially loves discounts, video games … and discounted video games. She previously wrote for Future PLC and Rakuten. She currently resides in northern Illinois with two fluffy cats. ... <a href=\"/author/louryn-strampe\">Read more</a>",
                "dangerousTitle": "Writer and Reviewer",
                "name": "Louryn Strampe",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b059259d2df7b4dab3b05/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "l0uryn",
                    "network": "twitter",
                    "label": "Follow Louryn Strampe on X"
                  }
                ],
                "url": "/author/louryn-strampe/"
              }
            ]
          }
        },
        "contentType": "gallery",
        "copilotID": "679a4ca2a944607be37796fe",
        "dangerousHed": "The Best Greens Powders",
        "dangerousDek": "We did the research (and taste-testing) for you to determine whether greens powders are worth your money, and if so, which ones.",
        "date": "02.05.2025",
        "pubDate": "2025-02-05T12:39:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "A reusable shaker bottle and packets and containers of nutrient powders. Background green leaf texture.",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Louryn Strampe; Kat Merck; Getty Images",
          "id": "67a28802ca5c5681a8e8b191",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_1024,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg",
              "srcset": "https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_120,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 120w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_240,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 240w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_320,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 320w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_640,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 640w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_960,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_1280,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg",
              "srcset": "https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_120,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 120w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_240,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 240w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_320,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 320w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_640,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 640w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_960,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 960w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_1280,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_1280,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg",
              "srcset": "https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_120,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 120w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_240,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 240w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_320,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 320w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_640,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 640w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_960,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 960w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_1280,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_1024,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg",
              "srcset": "https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_120,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 120w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_240,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 240w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_320,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 320w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_640,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 640w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_960,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_1280,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg",
              "srcset": "https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_120,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 120w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_240,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 240w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_320,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 320w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_640,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 640w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_960,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 960w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_1280,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 1280w"
            }
          },
          "masterAspectRatio": "2400:1800",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_1024,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg",
                "srcset": "https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_120,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 120w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_240,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 240w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_320,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 320w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_640,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 640w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/16:9/w_960,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_1280,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg",
                "srcset": "https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_120,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 120w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_240,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 240w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_320,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 320w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_640,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 640w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_960,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 960w, https://media.wired.com/photos/67a28802ca5c5681a8e8b191/3:2/w_1280,c_limit/Best%20Greens%20Powders%20Reviewer%20Collage%20022025%20SOURCE%20Louryn%20Strampe_Kat%20Merck.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "itemsCount": {
          "count": 6,
          "itemType": "slide"
        },
        "rubric": {
          "name": "Buying Guide"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "The Best Greens Powders",
          "dek": "We did the research (and taste-testing) for you to determine whether greens powders are worth your money, and if so, which ones."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/gallery/best-greens-powders/",
        "functionalTags": []
      },
      {
        "id": "67a11cf4e0fe35f643a4f9ef",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/ryan-waniata/\">Ryan Waniata</a> is a writer, editor, video host, and product reviewer with over 10 years of experience at sites including Digital Trends, Reviewed, Business Insider, Review Geek, and others. He’s evaluated everything from TVs and soundbars to smart gadgets and wearables, with a focus on A/V gear. He has a ... <a href=\"/author/ryan-waniata\">Read more</a>",
                "dangerousTitle": null,
                "name": "Ryan Waniata",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663a766c3fe811c0af69d628/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/663a766c3fe811c0af69d628/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [],
                "url": "/author/ryan-waniata/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "67a11cf4e0fe35f643a4f9ef",
        "dangerousHed": "The Best Super Bowl TV Deals",
        "dangerousDek": "Take your Super Bowl party to new heights with a great deal on a killer TV.",
        "date": "02.05.2025",
        "pubDate": "2025-02-05T12:03:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "LG C3 77inch OLED tv. Background light beige sand dunes.",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Amazon; Getty Images",
          "id": "67a294c41d9010d878342f8d",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_1024,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg",
              "srcset": "https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_120,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 120w, https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_240,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 240w, https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_320,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 320w, https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_640,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 640w, https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_960,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_1280,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg",
              "srcset": "https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_120,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 120w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_240,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 240w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_320,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 320w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_640,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 640w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_960,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 960w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_1280,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_1280,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg",
              "srcset": "https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_120,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 120w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_240,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 240w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_320,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 320w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_640,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 640w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_960,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 960w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_1280,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_1024,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg",
              "srcset": "https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_120,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 120w, https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_240,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 240w, https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_320,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 320w, https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_640,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 640w, https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_960,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_1280,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg",
              "srcset": "https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_120,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 120w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_240,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 240w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_320,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 320w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_640,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 640w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_960,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 960w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_1280,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 1280w"
            }
          },
          "masterAspectRatio": "2000:1300",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_1024,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg",
                "srcset": "https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_120,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 120w, https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_240,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 240w, https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_320,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 320w, https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_640,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 640w, https://media.wired.com/photos/67a294c41d9010d878342f8d/16:9/w_960,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_1280,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg",
                "srcset": "https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_120,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 120w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_240,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 240w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_320,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 320w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_640,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 640w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_960,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 960w, https://media.wired.com/photos/67a294c41d9010d878342f8d/3:2/w_1280,c_limit/LG-C3-77-inch-OLED-Abstract-Background-022025-SOURCE-Amazon.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Deals"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "The Best Super Bowl TV Deals",
          "dek": "Take your Super Bowl party to new heights with a great deal on a killer TV."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/the-best-super-bowl-tv-deals-2025/",
        "functionalTags": []
      },
      {
        "id": "678547daf78a91234db1e291",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/matt-reynolds/\">Matt Reynolds</a> is a senior writer at WIRED, where he covers climate, food, and biodiversity. Before that he was a technology journalist at New Scientist magazine. His first book, <em>The Future of Food: How to Feed the Planet Without Destroying It</em>, was published in 2021. Reynolds is a graduate of ... <a href=\"/author/matt-reynolds\">Read more</a>",
                "dangerousTitle": "Senior writer",
                "name": "Matt Reynolds",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e7134e454c690f3af289db/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e7134e454c690f3af289db/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "mattsreynolds1",
                    "network": "twitter",
                    "label": "Follow Matt Reynolds on X"
                  }
                ],
                "url": "/author/matt-reynolds/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "678547daf78a91234db1e291",
        "dangerousHed": "Early Detection Tools Help but They Can’t Stop Every Wildfire",
        "dangerousDek": "Tree-mounted sensors and new satellites promise a way to detect wildfires before they get out of hand&#8212;but no early detection method is foolproof.",
        "date": "02.05.2025",
        "pubDate": "2025-02-05T12:00:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "Water Waterfront Adult Person Photography Pier Bench Furniture Nature Outdoors and Scenery",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Marcus Ubungen/Getty Images",
          "id": "67859d5f007e4680400ee53e",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_1024,c_limit/science_remotefire_GettyImages-2192327272.jpg",
              "srcset": "https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_120,c_limit/science_remotefire_GettyImages-2192327272.jpg 120w, https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_240,c_limit/science_remotefire_GettyImages-2192327272.jpg 240w, https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_320,c_limit/science_remotefire_GettyImages-2192327272.jpg 320w, https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_640,c_limit/science_remotefire_GettyImages-2192327272.jpg 640w, https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_960,c_limit/science_remotefire_GettyImages-2192327272.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_1280,c_limit/science_remotefire_GettyImages-2192327272.jpg",
              "srcset": "https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_120,c_limit/science_remotefire_GettyImages-2192327272.jpg 120w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_240,c_limit/science_remotefire_GettyImages-2192327272.jpg 240w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_320,c_limit/science_remotefire_GettyImages-2192327272.jpg 320w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_640,c_limit/science_remotefire_GettyImages-2192327272.jpg 640w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_960,c_limit/science_remotefire_GettyImages-2192327272.jpg 960w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_1280,c_limit/science_remotefire_GettyImages-2192327272.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_1280,c_limit/science_remotefire_GettyImages-2192327272.jpg",
              "srcset": "https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_120,c_limit/science_remotefire_GettyImages-2192327272.jpg 120w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_240,c_limit/science_remotefire_GettyImages-2192327272.jpg 240w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_320,c_limit/science_remotefire_GettyImages-2192327272.jpg 320w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_640,c_limit/science_remotefire_GettyImages-2192327272.jpg 640w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_960,c_limit/science_remotefire_GettyImages-2192327272.jpg 960w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_1280,c_limit/science_remotefire_GettyImages-2192327272.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_1024,c_limit/science_remotefire_GettyImages-2192327272.jpg",
              "srcset": "https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_120,c_limit/science_remotefire_GettyImages-2192327272.jpg 120w, https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_240,c_limit/science_remotefire_GettyImages-2192327272.jpg 240w, https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_320,c_limit/science_remotefire_GettyImages-2192327272.jpg 320w, https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_640,c_limit/science_remotefire_GettyImages-2192327272.jpg 640w, https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_960,c_limit/science_remotefire_GettyImages-2192327272.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_1280,c_limit/science_remotefire_GettyImages-2192327272.jpg",
              "srcset": "https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_120,c_limit/science_remotefire_GettyImages-2192327272.jpg 120w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_240,c_limit/science_remotefire_GettyImages-2192327272.jpg 240w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_320,c_limit/science_remotefire_GettyImages-2192327272.jpg 320w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_640,c_limit/science_remotefire_GettyImages-2192327272.jpg 640w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_960,c_limit/science_remotefire_GettyImages-2192327272.jpg 960w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_1280,c_limit/science_remotefire_GettyImages-2192327272.jpg 1280w"
            }
          },
          "masterAspectRatio": "2400:1601",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_1024,c_limit/science_remotefire_GettyImages-2192327272.jpg",
                "srcset": "https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_120,c_limit/science_remotefire_GettyImages-2192327272.jpg 120w, https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_240,c_limit/science_remotefire_GettyImages-2192327272.jpg 240w, https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_320,c_limit/science_remotefire_GettyImages-2192327272.jpg 320w, https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_640,c_limit/science_remotefire_GettyImages-2192327272.jpg 640w, https://media.wired.com/photos/67859d5f007e4680400ee53e/16:9/w_960,c_limit/science_remotefire_GettyImages-2192327272.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_1280,c_limit/science_remotefire_GettyImages-2192327272.jpg",
                "srcset": "https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_120,c_limit/science_remotefire_GettyImages-2192327272.jpg 120w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_240,c_limit/science_remotefire_GettyImages-2192327272.jpg 240w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_320,c_limit/science_remotefire_GettyImages-2192327272.jpg 320w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_640,c_limit/science_remotefire_GettyImages-2192327272.jpg 640w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_960,c_limit/science_remotefire_GettyImages-2192327272.jpg 960w, https://media.wired.com/photos/67859d5f007e4680400ee53e/3:2/w_1280,c_limit/science_remotefire_GettyImages-2192327272.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "California Wildfires"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "Early Detection Tools Help but They Can’t Stop Every Wildfire",
          "dek": "Tree-mounted sensors and new satellites promise a way to detect wildfires before they get out of hand—but no early detection method is foolproof."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/early-detection-cant-stop-every-wildfire/",
        "functionalTags": []
      },
      {
        "id": "679d203a42d9dede15f552aa",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "Nena Farrell is a product writer and reviewer at WIRED, based in San Diego, California. She specializes in smart home gear, parenting, and textiles, and dabbles in a variety of other home and tech beats. Before joining WIRED, she covered smart home gear at The New York Times’ Wirecutter and ... <a href=\"/author/nena-farrell\">Read more</a>",
                "dangerousTitle": "Writer and Reviewer",
                "name": " Nena Farrell ",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [],
                "url": "/author/nena-farrell/"
              }
            ]
          }
        },
        "contentType": "gallery",
        "copilotID": "679d203a42d9dede15f552aa",
        "dangerousHed": "Our 15 Favorite Valentine’s Day Gifts and Date Ideas",
        "dangerousDek": "From editor-tested chocolates and flowers to at-home date night ideas, here’s everything we recommend gifting for the most romantic holiday of the year.",
        "date": "02.05.2025",
        "pubDate": "2025-02-05T11:32:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "A small white book a candle and a gold smart ring. Background soft pink watercolor texture.",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: The Adventure Challenge; Maude; Oura; Getty Images",
          "id": "67a2911bafbdf74f538799f4",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_1024,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg",
              "srcset": "https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_120,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 120w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_240,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 240w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_320,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 320w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_640,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 640w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_960,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_1280,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg",
              "srcset": "https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_120,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 120w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_240,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 240w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_320,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 320w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_640,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 640w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_960,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 960w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_1280,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_1280,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg",
              "srcset": "https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_120,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 120w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_240,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 240w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_320,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 320w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_640,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 640w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_960,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 960w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_1280,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_1024,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg",
              "srcset": "https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_120,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 120w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_240,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 240w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_320,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 320w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_640,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 640w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_960,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_1280,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg",
              "srcset": "https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_120,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 120w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_240,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 240w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_320,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 320w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_640,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 640w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_960,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 960w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_1280,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 1280w"
            }
          },
          "masterAspectRatio": "2000:1300",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_1024,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg",
                "srcset": "https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_120,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 120w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_240,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 240w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_320,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 320w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_640,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 640w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/16:9/w_960,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_1280,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg",
                "srcset": "https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_120,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 120w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_240,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 240w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_320,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 320w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_640,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 640w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_960,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 960w, https://media.wired.com/photos/67a2911bafbdf74f538799f4/3:2/w_1280,c_limit/Valentine's%20Day%20Gifts%20Abstract%20Background%20022025.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "itemsCount": {
          "count": 15,
          "itemType": "slide"
        },
        "rubric": {
          "name": "Sweet Hearts"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "Our 15 Favorite Valentine’s Day Gifts and Date Ideas",
          "dek": "From editor-tested chocolates and flowers to at-home date night ideas, here’s everything we recommend gifting for the most romantic holiday of the year."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/gallery/best-valentines-day-gifts/",
        "functionalTags": []
      },
      {
        "id": "67a2754e0a98743a8c789000",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/reece-rogers/\">Reece Rogers</a> is WIRED&#39;s service writer, focused on explaining crucial topics and helping readers get the most out of their technology. He is the author of the popular <a href=\"https://www.wired.com/newsletter/ai-unlocked?sourceCode=AuthorBio\" target=\"_blank\"><em>AI Unlocked</em> newsletter series</a> that helps you make the most of AI tools&#8212;<a href=\"https://www.wired.com/newsletter/ai-unlocked?sourceCode=AuthorBio\" target=\"_blank\"><strong>sign up here</strong></a>. Prior to WIRED, Reece covered streaming at ... <a href=\"/author/reece-rogers\">Read more</a>",
                "dangerousTitle": "Service Writer",
                "name": "Reece Rogers",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/635b05abbaca2e722bfbc6f4/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [],
                "url": "/author/reece-rogers/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "67a2754e0a98743a8c789000",
        "dangerousHed": "How to Watch the 2025 Super Bowl and Halftime Show for Free",
        "dangerousDek": "The game between the Philadelphia Eagles and Kansas City Chiefs, with a halftime show by Kendrick Lamar, takes place on Sunday February 9. Here&#39;s how to tune in.",
        "date": "02.05.2025",
        "pubDate": "2025-02-05T11:00:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "Search",
          "caption": "",
          "contentType": "photo",
          "credit": "Photo-Illustration: Wired Staff; Kevin Sabitus/Getty Images",
          "id": "67a281f91d9010d878342f8b",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_1024,c_limit/superbowl-watch-gear-2197644372.jpg",
              "srcset": "https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_120,c_limit/superbowl-watch-gear-2197644372.jpg 120w, https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_240,c_limit/superbowl-watch-gear-2197644372.jpg 240w, https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_320,c_limit/superbowl-watch-gear-2197644372.jpg 320w, https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_640,c_limit/superbowl-watch-gear-2197644372.jpg 640w, https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_960,c_limit/superbowl-watch-gear-2197644372.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_1280,c_limit/superbowl-watch-gear-2197644372.jpg",
              "srcset": "https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_120,c_limit/superbowl-watch-gear-2197644372.jpg 120w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_240,c_limit/superbowl-watch-gear-2197644372.jpg 240w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_320,c_limit/superbowl-watch-gear-2197644372.jpg 320w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_640,c_limit/superbowl-watch-gear-2197644372.jpg 640w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_960,c_limit/superbowl-watch-gear-2197644372.jpg 960w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_1280,c_limit/superbowl-watch-gear-2197644372.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_1280,c_limit/superbowl-watch-gear-2197644372.jpg",
              "srcset": "https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_120,c_limit/superbowl-watch-gear-2197644372.jpg 120w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_240,c_limit/superbowl-watch-gear-2197644372.jpg 240w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_320,c_limit/superbowl-watch-gear-2197644372.jpg 320w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_640,c_limit/superbowl-watch-gear-2197644372.jpg 640w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_960,c_limit/superbowl-watch-gear-2197644372.jpg 960w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_1280,c_limit/superbowl-watch-gear-2197644372.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_1024,c_limit/superbowl-watch-gear-2197644372.jpg",
              "srcset": "https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_120,c_limit/superbowl-watch-gear-2197644372.jpg 120w, https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_240,c_limit/superbowl-watch-gear-2197644372.jpg 240w, https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_320,c_limit/superbowl-watch-gear-2197644372.jpg 320w, https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_640,c_limit/superbowl-watch-gear-2197644372.jpg 640w, https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_960,c_limit/superbowl-watch-gear-2197644372.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_1280,c_limit/superbowl-watch-gear-2197644372.jpg",
              "srcset": "https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_120,c_limit/superbowl-watch-gear-2197644372.jpg 120w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_240,c_limit/superbowl-watch-gear-2197644372.jpg 240w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_320,c_limit/superbowl-watch-gear-2197644372.jpg 320w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_640,c_limit/superbowl-watch-gear-2197644372.jpg 640w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_960,c_limit/superbowl-watch-gear-2197644372.jpg 960w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_1280,c_limit/superbowl-watch-gear-2197644372.jpg 1280w"
            }
          },
          "masterAspectRatio": "2400:1600",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_1024,c_limit/superbowl-watch-gear-2197644372.jpg",
                "srcset": "https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_120,c_limit/superbowl-watch-gear-2197644372.jpg 120w, https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_240,c_limit/superbowl-watch-gear-2197644372.jpg 240w, https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_320,c_limit/superbowl-watch-gear-2197644372.jpg 320w, https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_640,c_limit/superbowl-watch-gear-2197644372.jpg 640w, https://media.wired.com/photos/67a281f91d9010d878342f8b/16:9/w_960,c_limit/superbowl-watch-gear-2197644372.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_1280,c_limit/superbowl-watch-gear-2197644372.jpg",
                "srcset": "https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_120,c_limit/superbowl-watch-gear-2197644372.jpg 120w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_240,c_limit/superbowl-watch-gear-2197644372.jpg 240w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_320,c_limit/superbowl-watch-gear-2197644372.jpg 320w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_640,c_limit/superbowl-watch-gear-2197644372.jpg 640w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_960,c_limit/superbowl-watch-gear-2197644372.jpg 960w, https://media.wired.com/photos/67a281f91d9010d878342f8b/3:2/w_1280,c_limit/superbowl-watch-gear-2197644372.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "GNXFL"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "How to Watch the 2025 Super Bowl and Halftime Show for Free",
          "dek": "The game between the Philadelphia Eagles and Kansas City Chiefs, with a halftime show by Kendrick Lamar, takes place on Sunday February 9. Here's how to tune in."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/how-to-watch-super-bowl-2025-free-halftime-show/",
        "functionalTags": []
      },
      {
        "id": "67100c9a82459143cee93f27",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/scott-gilbertson/\">Scott Gilbertson</a> is Operations Manager for the WIRED Reviews Team. He was previously a writer and editor for WIRED’s Webmonkey.com, covering the independent web and early internet culture. You can reach him at luxagraf.net. ... <a href=\"/author/scott-gilbertson\">Read more</a>",
                "dangerousTitle": "Senior Writer and Reviewer",
                "name": "Scott Gilbertson",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e83f330a21dec3d34419f2/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "luxagraf",
                    "network": "twitter",
                    "label": "Follow Scott Gilbertson on X"
                  }
                ],
                "url": "/author/scott-gilbertson/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "67100c9a82459143cee93f27",
        "dangerousHed": "Top NordVPN Coupons: 74% Off + 3 Months Free",
        "dangerousDek": "Save 74% on 2-year plans and get 3 free months with our NordVPN discount codes.",
        "date": "02.05.2025",
        "pubDate": "2025-02-05T06:00:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "Image may contain Text Nature Outdoors and Sky",
          "caption": "",
          "contentType": "photo",
          "credit": "ILLUSTRATION: GETTY IMAGES",
          "id": "66ea076fca863bb4c1028b64",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_1024,c_limit/WIRED-Coupons-11.jpg",
              "srcset": "https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_120,c_limit/WIRED-Coupons-11.jpg 120w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_240,c_limit/WIRED-Coupons-11.jpg 240w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_320,c_limit/WIRED-Coupons-11.jpg 320w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_640,c_limit/WIRED-Coupons-11.jpg 640w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_960,c_limit/WIRED-Coupons-11.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_1280,c_limit/WIRED-Coupons-11.jpg",
              "srcset": "https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_120,c_limit/WIRED-Coupons-11.jpg 120w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_240,c_limit/WIRED-Coupons-11.jpg 240w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_320,c_limit/WIRED-Coupons-11.jpg 320w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_640,c_limit/WIRED-Coupons-11.jpg 640w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_960,c_limit/WIRED-Coupons-11.jpg 960w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_1280,c_limit/WIRED-Coupons-11.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_1280,c_limit/WIRED-Coupons-11.jpg",
              "srcset": "https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_120,c_limit/WIRED-Coupons-11.jpg 120w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_240,c_limit/WIRED-Coupons-11.jpg 240w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_320,c_limit/WIRED-Coupons-11.jpg 320w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_640,c_limit/WIRED-Coupons-11.jpg 640w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_960,c_limit/WIRED-Coupons-11.jpg 960w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_1280,c_limit/WIRED-Coupons-11.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_1024,c_limit/WIRED-Coupons-11.jpg",
              "srcset": "https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_120,c_limit/WIRED-Coupons-11.jpg 120w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_240,c_limit/WIRED-Coupons-11.jpg 240w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_320,c_limit/WIRED-Coupons-11.jpg 320w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_640,c_limit/WIRED-Coupons-11.jpg 640w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_960,c_limit/WIRED-Coupons-11.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_1280,c_limit/WIRED-Coupons-11.jpg",
              "srcset": "https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_120,c_limit/WIRED-Coupons-11.jpg 120w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_240,c_limit/WIRED-Coupons-11.jpg 240w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_320,c_limit/WIRED-Coupons-11.jpg 320w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_640,c_limit/WIRED-Coupons-11.jpg 640w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_960,c_limit/WIRED-Coupons-11.jpg 960w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_1280,c_limit/WIRED-Coupons-11.jpg 1280w"
            }
          },
          "masterAspectRatio": "1734:1300",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_1024,c_limit/WIRED-Coupons-11.jpg",
                "srcset": "https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_120,c_limit/WIRED-Coupons-11.jpg 120w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_240,c_limit/WIRED-Coupons-11.jpg 240w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_320,c_limit/WIRED-Coupons-11.jpg 320w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_640,c_limit/WIRED-Coupons-11.jpg 640w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/16:9/w_960,c_limit/WIRED-Coupons-11.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_1280,c_limit/WIRED-Coupons-11.jpg",
                "srcset": "https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_120,c_limit/WIRED-Coupons-11.jpg 120w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_240,c_limit/WIRED-Coupons-11.jpg 240w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_320,c_limit/WIRED-Coupons-11.jpg 320w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_640,c_limit/WIRED-Coupons-11.jpg 640w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_960,c_limit/WIRED-Coupons-11.jpg 960w, https://media.wired.com/photos/66ea076fca863bb4c1028b64/3:2/w_1280,c_limit/WIRED-Coupons-11.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Coupons"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "Top NordVPN Coupons: 74% Off \\+ 3 Months Free",
          "dek": "Save 74% on 2-year plans and get 3 free months with our NordVPN discount codes."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/nordvpn-coupon/",
        "functionalTags": []
      },
      {
        "id": "679a8a86d6b6d26aee985e2a",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/zeyi-yang/\">Zeyi Yang</a> is a senior writer at WIRED, covering technology and business in China. Prior to joining WIRED he was China reporter at MIT Technology Review and a tech reporter at Protocol. His journalism has appeared in other publications such as Rest of World, Columbia Journalism Review, and Nikkei Asia. ... <a href=\"/author/zeyi-yang\">Read more</a>",
                "dangerousTitle": "Senior writer",
                "name": "Zeyi Yang",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/67607c65419cea5d9e32a07f/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [],
                "url": "/author/zeyi-yang/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "679a8a86d6b6d26aee985e2a",
        "dangerousHed": "USPS Resumes Accepting Packages From China After Unexpected Suspension",
        "dangerousDek": "As part of new tariffs on Chinese imports, President Donald Trump eliminated an exemption for small packages, vastly increasing the amount of parcels US Customs and Border Protection needs to inspect.",
        "date": "02.04.2025",
        "pubDate": "2025-02-05T03:33:47.229Z",
        "issueDate": "",
        "image": {
          "altText": "A package from Temu among with other packages.",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Nikos Pekiaridis/Getty Images",
          "id": "67a12cc0505b682bfc87af73",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_1024,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg",
              "srcset": "https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_120,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 120w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_240,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 240w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_320,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 320w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_640,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 640w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_960,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_1280,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg",
              "srcset": "https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_120,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 120w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_240,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 240w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_320,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 320w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_640,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 640w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_960,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 960w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_1280,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_1280,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg",
              "srcset": "https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_120,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 120w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_240,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 240w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_320,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 320w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_640,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 640w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_960,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 960w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_1280,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_1024,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg",
              "srcset": "https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_120,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 120w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_240,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 240w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_320,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 320w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_640,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 640w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_960,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_1280,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg",
              "srcset": "https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_120,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 120w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_240,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 240w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_320,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 320w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_640,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 640w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_960,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 960w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_1280,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 1280w"
            }
          },
          "masterAspectRatio": "2000:1333",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_1024,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg",
                "srcset": "https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_120,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 120w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_240,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 240w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_320,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 320w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_640,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 640w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/16:9/w_960,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_1280,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg",
                "srcset": "https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_120,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 120w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_240,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 240w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_320,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 320w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_640,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 640w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_960,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 960w, https://media.wired.com/photos/67a12cc0505b682bfc87af73/3:2/w_1280,c_limit/Trump-Tariff-Temu-Packages-Business-1653668805.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Tracking Unavailable "
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "USPS Resumes Accepting Packages From China After Unexpected Suspension",
          "dek": "As part of new tariffs on Chinese imports, President Donald Trump eliminated an exemption for small packages, vastly increasing the amount of parcels US Customs and Border Protection needs to inspect."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/tariffs-trump-ecommerce-amazon-temu/",
        "functionalTags": []
      },
      {
        "id": "67a29bed5c653e9f235520e6",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/kate-knibbs/\">Kate Knibbs</a> is a senior writer at WIRED, covering the human side of the generative AI boom and how new tech shapes the arts, entertainment, and media industries. Prior to joining WIRED she was a features writer at The Ringer and a senior writer at Gizmodo. She is based in ... <a href=\"/author/kate-knibbs\">Read more</a>",
                "dangerousTitle": "Senior Writer",
                "name": "Kate Knibbs",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/640642d1369bdab06d01df9a/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/640642d1369bdab06d01df9a/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "Knibbs",
                    "network": "twitter",
                    "label": "Follow Kate Knibbs on X"
                  }
                ],
                "url": "/author/kate-knibbs/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "67a29bed5c653e9f235520e6",
        "dangerousHed": "State Department Puts ‘All Direct Hire’ USAID Personnel on Administrative Leave",
        "dangerousDek": "The US government’s primary foreign aid agency has employees stationed all over the world, many of whom are now bracing to abruptly leave their posts.",
        "date": "02.04.2025",
        "pubDate": "2025-02-05T02:36:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "WASHINGTON DC  FEBRUARY 03 The U.S. Agency for International Development  headquarters is seen on February 03 2025 in...",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Kevin Dietsch/Getty Images",
          "id": "67a29e64fbbb289f408c3105",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_1024,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg",
              "srcset": "https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_120,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 120w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_240,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 240w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_320,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 320w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_640,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 640w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_960,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_1280,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg",
              "srcset": "https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_120,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 120w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_240,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 240w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_320,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 320w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_640,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 640w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_960,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 960w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_1280,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_1280,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg",
              "srcset": "https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_120,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 120w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_240,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 240w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_320,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 320w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_640,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 640w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_960,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 960w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_1280,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_1024,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg",
              "srcset": "https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_120,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 120w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_240,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 240w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_320,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 320w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_640,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 640w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_960,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_1280,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg",
              "srcset": "https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_120,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 120w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_240,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 240w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_320,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 320w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_640,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 640w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_960,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 960w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_1280,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 1280w"
            }
          },
          "masterAspectRatio": "2000:1322",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_1024,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg",
                "srcset": "https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_120,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 120w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_240,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 240w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_320,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 320w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_640,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 640w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/16:9/w_960,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_1280,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg",
                "srcset": "https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_120,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 120w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_240,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 240w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_320,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 320w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_640,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 640w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_960,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 960w, https://media.wired.com/photos/67a29e64fbbb289f408c3105/3:2/w_1280,c_limit/Ttump-USAID-Global-Employees-Politics-2197436148.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Unplanned Travel"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "State Department Puts ‘All Direct Hire’ USAID Personnel on Administrative Leave",
          "dek": "The US government’s primary foreign aid agency has employees stationed all over the world, many of whom are now bracing to abruptly leave their posts."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/chaos-usaid-staffers-sent-home/",
        "functionalTags": []
      },
      {
        "id": "67a266ab597d41042eba2e1d",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/paresh-dave/\">Paresh Dave</a> is a senior writer for WIRED, covering the inner workings of Big Tech companies. He writes about how apps and gadgets are built and about their impacts while giving voice to the stories of the <a href=\"https://www.reuters.com/business/sustainable-business/exclusive-google-searches-new-measure-skin-tones-curb-bias-products-2021-06-18/\">underappreciated</a> and <a href=\"https://www.reuters.com/technology/elon-musk-orders-removal-twitter-suicide-prevention-feature-sources-say-2022-12-23/\">disadvantaged</a>. He was previously a reporter for Reuters and the Los Angeles Times, ... <a href=\"/author/paresh-dave\">Read more</a>",
                "dangerousTitle": "Senior Writer",
                "name": "Paresh Dave",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [],
                "url": "/author/paresh-dave/"
              },
              {
                "dangerousBio": "<a href=\"/author/caroline-haskins/\">Caroline Haskins</a> is a freelance reporter based in New York covering tech with a focus on politics, labor, and culture. She has previously worked as a staff reporter at Business Insider, BuzzFeed News, and Vice&#39;s Motherboard, and as a research editor at Business Insider.\nYou can send her tips via email ... <a href=\"/author/caroline-haskins\">Read more</a>",
                "dangerousTitle": null,
                "name": "Caroline Haskins",
                "socialMedia": [],
                "url": "/author/caroline-haskins/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "67a266ab597d41042eba2e1d",
        "dangerousHed": "Google Lifts a Ban on Using Its AI for Weapons and Surveillance",
        "dangerousDek": "Google published principles in 2018 barring its AI technology from being used for sensitive purposes. Weeks into President Donald Trump’s second term, those guidelines are being overhauled.",
        "date": "02.04.2025",
        "pubDate": "2025-02-04T20:47:25.226Z",
        "issueDate": "",
        "image": {
          "altText": "The Google Bay View campus in Mountain View California US on Tuesday Nov. 28 2023. Google said in March 2022 that it...",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Mike Kai Chen/Getty Images",
          "id": "67a26946d4e8f75a24ee7c21",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_1024,c_limit/Google-AI-Principles-Business-2076708246.jpg",
              "srcset": "https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_120,c_limit/Google-AI-Principles-Business-2076708246.jpg 120w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_240,c_limit/Google-AI-Principles-Business-2076708246.jpg 240w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_320,c_limit/Google-AI-Principles-Business-2076708246.jpg 320w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_640,c_limit/Google-AI-Principles-Business-2076708246.jpg 640w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_960,c_limit/Google-AI-Principles-Business-2076708246.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_1280,c_limit/Google-AI-Principles-Business-2076708246.jpg",
              "srcset": "https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_120,c_limit/Google-AI-Principles-Business-2076708246.jpg 120w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_240,c_limit/Google-AI-Principles-Business-2076708246.jpg 240w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_320,c_limit/Google-AI-Principles-Business-2076708246.jpg 320w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_640,c_limit/Google-AI-Principles-Business-2076708246.jpg 640w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_960,c_limit/Google-AI-Principles-Business-2076708246.jpg 960w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_1280,c_limit/Google-AI-Principles-Business-2076708246.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_1280,c_limit/Google-AI-Principles-Business-2076708246.jpg",
              "srcset": "https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_120,c_limit/Google-AI-Principles-Business-2076708246.jpg 120w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_240,c_limit/Google-AI-Principles-Business-2076708246.jpg 240w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_320,c_limit/Google-AI-Principles-Business-2076708246.jpg 320w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_640,c_limit/Google-AI-Principles-Business-2076708246.jpg 640w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_960,c_limit/Google-AI-Principles-Business-2076708246.jpg 960w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_1280,c_limit/Google-AI-Principles-Business-2076708246.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_1024,c_limit/Google-AI-Principles-Business-2076708246.jpg",
              "srcset": "https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_120,c_limit/Google-AI-Principles-Business-2076708246.jpg 120w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_240,c_limit/Google-AI-Principles-Business-2076708246.jpg 240w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_320,c_limit/Google-AI-Principles-Business-2076708246.jpg 320w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_640,c_limit/Google-AI-Principles-Business-2076708246.jpg 640w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_960,c_limit/Google-AI-Principles-Business-2076708246.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_1280,c_limit/Google-AI-Principles-Business-2076708246.jpg",
              "srcset": "https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_120,c_limit/Google-AI-Principles-Business-2076708246.jpg 120w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_240,c_limit/Google-AI-Principles-Business-2076708246.jpg 240w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_320,c_limit/Google-AI-Principles-Business-2076708246.jpg 320w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_640,c_limit/Google-AI-Principles-Business-2076708246.jpg 640w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_960,c_limit/Google-AI-Principles-Business-2076708246.jpg 960w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_1280,c_limit/Google-AI-Principles-Business-2076708246.jpg 1280w"
            }
          },
          "masterAspectRatio": "2000:1333",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_1024,c_limit/Google-AI-Principles-Business-2076708246.jpg",
                "srcset": "https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_120,c_limit/Google-AI-Principles-Business-2076708246.jpg 120w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_240,c_limit/Google-AI-Principles-Business-2076708246.jpg 240w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_320,c_limit/Google-AI-Principles-Business-2076708246.jpg 320w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_640,c_limit/Google-AI-Principles-Business-2076708246.jpg 640w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/16:9/w_960,c_limit/Google-AI-Principles-Business-2076708246.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_1280,c_limit/Google-AI-Principles-Business-2076708246.jpg",
                "srcset": "https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_120,c_limit/Google-AI-Principles-Business-2076708246.jpg 120w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_240,c_limit/Google-AI-Principles-Business-2076708246.jpg 240w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_320,c_limit/Google-AI-Principles-Business-2076708246.jpg 320w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_640,c_limit/Google-AI-Principles-Business-2076708246.jpg 640w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_960,c_limit/Google-AI-Principles-Business-2076708246.jpg 960w, https://media.wired.com/photos/67a26946d4e8f75a24ee7c21/3:2/w_1280,c_limit/Google-AI-Principles-Business-2076708246.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Principles 2.0"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "Google Lifts a Ban on Using Its AI for Weapons and Surveillance",
          "dek": "Google published principles in 2018 barring its AI technology from being used for sensitive purposes. Weeks into President Donald Trump’s second term, those guidelines are being overhauled."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/google-responsible-ai-principles/",
        "functionalTags": []
      },
      {
        "id": "679817ef36209dd3711e499b",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "Nena Farrell is a product writer and reviewer at WIRED, based in San Diego, California. She specializes in smart home gear, parenting, and textiles, and dabbles in a variety of other home and tech beats. Before joining WIRED, she covered smart home gear at The New York Times’ Wirecutter and ... <a href=\"/author/nena-farrell\">Read more</a>",
                "dangerousTitle": "Writer and Reviewer",
                "name": " Nena Farrell ",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65563baf946aa0b0131abf3e/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [],
                "url": "/author/nena-farrell/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "679817ef36209dd3711e499b",
        "dangerousHed": "The Best Early Presidents’ Day Mattress Deals (and Bedding Too!)",
        "dangerousDek": "It’s one of the best times of year to invest in a mattress, pillows, and sheets. Here’s everything we recommend buying and who has the best sales ahead of Presidents’ Day weekend.",
        "date": "02.04.2025",
        "pubDate": "2025-02-04T20:27:44.482Z",
        "issueDate": "",
        "image": {
          "altText": "Bedgear Split Head M3 Performance Mattress on a pixelated green background",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Bedgear; Getty Images",
          "id": "67a248a93f85a9d84885eb03",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_1024,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg",
              "srcset": "https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_120,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 120w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_240,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 240w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_320,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 320w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_640,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 640w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_960,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_1280,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg",
              "srcset": "https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_120,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 120w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_240,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 240w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_320,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 320w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_640,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 640w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_960,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 960w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_1280,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_1280,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg",
              "srcset": "https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_120,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 120w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_240,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 240w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_320,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 320w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_640,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 640w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_960,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 960w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_1280,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_1024,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg",
              "srcset": "https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_120,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 120w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_240,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 240w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_320,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 320w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_640,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 640w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_960,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_1280,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg",
              "srcset": "https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_120,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 120w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_240,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 240w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_320,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 320w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_640,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 640w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_960,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 960w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_1280,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 1280w"
            }
          },
          "masterAspectRatio": "2000:1300",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_1024,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg",
                "srcset": "https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_120,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 120w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_240,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 240w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_320,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 320w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_640,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 640w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/16:9/w_960,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_1280,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg",
                "srcset": "https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_120,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 120w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_240,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 240w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_320,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 320w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_640,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 640w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_960,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 960w, https://media.wired.com/photos/67a248a93f85a9d84885eb03/3:2/w_1280,c_limit/Bedgear%20Split%20Head%20M3%20Performance%20Mattress%20Abstract%20Background%20022025%20SOURCE%20Bedgear.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Dreamy Deals"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "The Best Early Presidents’ Day Mattress Deals (and Bedding Too\\!)",
          "dek": "It's one of the best times of year to invest in a mattress, pillows, and sheets. Here’s everything we recommend buying and who has the best sales ahead of Presidents’ Day weekend."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/presidents-day-mattress-deals-2025/",
        "functionalTags": []
      },
      {
        "id": "63d96ba473cac2b11b42eaae",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/jennifer-m-wood/\">Jennifer M. Wood</a> writes about movies, television, and pop culture. She is the editor of <em>The Curious Viewer: A Miscellany of Bingeable Streaming TV Shows from the Past Twenty Years</em> and the author of <em>The Curious Movie Buff: A Miscellany of Fantastic Films from the Past 50 Years</em>.  ... <a href=\"/author/jennifer-m-wood\">Read more</a>",
                "dangerousTitle": null,
                "name": "Jennifer M. Wood",
                "socialMedia": [],
                "url": "/author/jennifer-m-wood/"
              },
              {
                "dangerousBio": null,
                "dangerousTitle": null,
                "name": "WIRED Staff",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835b23a5924e619dc4485/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e835b23a5924e619dc4485/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [],
                "url": "/author/wired-staff/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "63d96ba473cac2b11b42eaae",
        "dangerousHed": "The 44 Best Shows on Hulu Right Now",
        "dangerousDek": "<em>Paradise, Scamanda</em>, and <em>What We Do in the Shadows</em> are just a few of the shows you should be watching on Hulu this month.",
        "date": "02.04.2025",
        "pubDate": "2025-02-04T20:00:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "PARADISE  Wildcat IS Down  It's just another day in Paradise until Agent Xavier Collins discovers one of the world's...",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Ser Baffo/Hulu",
          "id": "679bfb419795a436b9a5a116",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_1024,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg",
              "srcset": "https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_120,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 120w, https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_240,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 240w, https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_320,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 320w, https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_640,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 640w, https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_960,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_1280,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg",
              "srcset": "https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_120,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 120w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_240,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 240w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_320,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 320w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_640,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 640w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_960,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 960w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_1280,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_1280,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg",
              "srcset": "https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_120,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 120w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_240,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 240w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_320,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 320w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_640,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 640w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_960,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 960w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_1280,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_1024,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg",
              "srcset": "https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_120,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 120w, https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_240,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 240w, https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_320,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 320w, https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_640,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 640w, https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_960,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_1280,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg",
              "srcset": "https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_120,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 120w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_240,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 240w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_320,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 320w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_640,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 640w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_960,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 960w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_1280,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 1280w"
            }
          },
          "masterAspectRatio": "2000:1600",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_1024,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg",
                "srcset": "https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_120,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 120w, https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_240,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 240w, https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_320,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 320w, https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_640,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 640w, https://media.wired.com/photos/679bfb419795a436b9a5a116/16:9/w_960,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_1280,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg",
                "srcset": "https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_120,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 120w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_240,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 240w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_320,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 320w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_640,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 640w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_960,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 960w, https://media.wired.com/photos/679bfb419795a436b9a5a116/3:2/w_1280,c_limit/Hulu-Show-Guide-Paradise-Culture-171889_0016r.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Culture Guides"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "The 44 Best Shows on Hulu Right Now",
          "dek": "*Paradise, Scamanda*, and *What We Do in the Shadows* are just a few of the shows you should be watching on Hulu this month."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/best-tv-shows-hulu-this-week/",
        "functionalTags": []
      },
      {
        "id": "67a233e82b7b64098e0700c3",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/paresh-dave/\">Paresh Dave</a> is a senior writer for WIRED, covering the inner workings of Big Tech companies. He writes about how apps and gadgets are built and about their impacts while giving voice to the stories of the <a href=\"https://www.reuters.com/business/sustainable-business/exclusive-google-searches-new-measure-skin-tones-curb-bias-products-2021-06-18/\">underappreciated</a> and <a href=\"https://www.reuters.com/technology/elon-musk-orders-removal-twitter-suicide-prevention-feature-sources-say-2022-12-23/\">disadvantaged</a>. He was previously a reporter for Reuters and the Los Angeles Times, ... <a href=\"/author/paresh-dave\">Read more</a>",
                "dangerousTitle": "Senior Writer",
                "name": "Paresh Dave",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/645addcb0a0f9ed43773ef84/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [],
                "url": "/author/paresh-dave/"
              },
              {
                "dangerousBio": "<a href=\"/author/louise-matsakis/\">Louise Matsakis</a> is a senior business editor at WIRED. She was previously deputy news editor at Semafor, a senior editor at Rest of World, and a staff writer at WIRED. An investigation she cowrote on the Chinese fast-fashion giant Shein won the 2022 Society of Publishers in Asia award for ... <a href=\"/author/louise-matsakis\">Read more</a>",
                "dangerousTitle": "Senior Business Editor",
                "name": "Louise Matsakis",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e83365e34ce69a22d7feb1/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "lmatsakis",
                    "network": "twitter",
                    "label": "Follow Louise Matsakis on X"
                  }
                ],
                "url": "/author/louise-matsakis/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "67a233e82b7b64098e0700c3",
        "dangerousHed": "China Is Investigating Google Over Trump’s Tariffs",
        "dangerousDek": "Google’s limited presence in China gives Beijing room to hit back harder if President Donald Trump’s trade war escalates.",
        "date": "02.04.2025",
        "pubDate": "2025-02-04T17:13:52.840Z",
        "issueDate": "",
        "image": {
          "altText": "chinese flag",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Getty Images",
          "id": "67a242f3fbbb289f408c30fc",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_1024,c_limit/china-google-biz-513226286.jpg",
              "srcset": "https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_120,c_limit/china-google-biz-513226286.jpg 120w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_240,c_limit/china-google-biz-513226286.jpg 240w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_320,c_limit/china-google-biz-513226286.jpg 320w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_640,c_limit/china-google-biz-513226286.jpg 640w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_960,c_limit/china-google-biz-513226286.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_1280,c_limit/china-google-biz-513226286.jpg",
              "srcset": "https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_120,c_limit/china-google-biz-513226286.jpg 120w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_240,c_limit/china-google-biz-513226286.jpg 240w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_320,c_limit/china-google-biz-513226286.jpg 320w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_640,c_limit/china-google-biz-513226286.jpg 640w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_960,c_limit/china-google-biz-513226286.jpg 960w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_1280,c_limit/china-google-biz-513226286.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_1280,c_limit/china-google-biz-513226286.jpg",
              "srcset": "https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_120,c_limit/china-google-biz-513226286.jpg 120w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_240,c_limit/china-google-biz-513226286.jpg 240w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_320,c_limit/china-google-biz-513226286.jpg 320w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_640,c_limit/china-google-biz-513226286.jpg 640w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_960,c_limit/china-google-biz-513226286.jpg 960w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_1280,c_limit/china-google-biz-513226286.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_1024,c_limit/china-google-biz-513226286.jpg",
              "srcset": "https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_120,c_limit/china-google-biz-513226286.jpg 120w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_240,c_limit/china-google-biz-513226286.jpg 240w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_320,c_limit/china-google-biz-513226286.jpg 320w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_640,c_limit/china-google-biz-513226286.jpg 640w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_960,c_limit/china-google-biz-513226286.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_1280,c_limit/china-google-biz-513226286.jpg",
              "srcset": "https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_120,c_limit/china-google-biz-513226286.jpg 120w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_240,c_limit/china-google-biz-513226286.jpg 240w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_320,c_limit/china-google-biz-513226286.jpg 320w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_640,c_limit/china-google-biz-513226286.jpg 640w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_960,c_limit/china-google-biz-513226286.jpg 960w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_1280,c_limit/china-google-biz-513226286.jpg 1280w"
            }
          },
          "masterAspectRatio": "2400:1350",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_1024,c_limit/china-google-biz-513226286.jpg",
                "srcset": "https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_120,c_limit/china-google-biz-513226286.jpg 120w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_240,c_limit/china-google-biz-513226286.jpg 240w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_320,c_limit/china-google-biz-513226286.jpg 320w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_640,c_limit/china-google-biz-513226286.jpg 640w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/16:9/w_960,c_limit/china-google-biz-513226286.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_1280,c_limit/china-google-biz-513226286.jpg",
                "srcset": "https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_120,c_limit/china-google-biz-513226286.jpg 120w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_240,c_limit/china-google-biz-513226286.jpg 240w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_320,c_limit/china-google-biz-513226286.jpg 320w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_640,c_limit/china-google-biz-513226286.jpg 640w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_960,c_limit/china-google-biz-513226286.jpg 960w, https://media.wired.com/photos/67a242f3fbbb289f408c30fc/3:2/w_1280,c_limit/china-google-biz-513226286.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Retaliation"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "China Is Investigating Google Over Trump’s Tariffs",
          "dek": "Google’s limited presence in China gives Beijing room to hit back harder if President Donald Trump’s trade war escalates."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/google-china-antitrust-trump-tariffs/",
        "functionalTags": []
      },
      {
        "id": "67a16cded336e84dd2ba97dd",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/dell-cameron/\">Dell Cameron</a> is an investigative reporter from Texas covering privacy and national security. He&#39;s the recipient of multiple Society of Professional Journalists awards and is co-recipient of an Edward R. Murrow Award for Investigative Reporting. Previously, he was a senior reporter at Gizmodo and a staff writer for the Daily ... <a href=\"/author/dell-cameron\">Read more</a>",
                "dangerousTitle": "Senior Reporter, National Security",
                "name": "Dell Cameron",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/663fe63cf59145e49d5e32df/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "dellcameron.me",
                    "network": "website",
                    "label": "Follow Dell Cameron on Website"
                  }
                ],
                "url": "/author/dell-cameron/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "67a16cded336e84dd2ba97dd",
        "dangerousHed": "Federal Workers Sue to Disconnect DOGE Server",
        "dangerousDek": "Two federal workers, citing reports that Elon Musk’s associates are operating an illegally connected email server at OPM, seek a restraining order.",
        "date": "02.04.2025",
        "pubDate": "2025-02-04T16:24:19.165Z",
        "issueDate": "",
        "image": {
          "altText": "WASHINGTON DC  FEBRUARY 03 The Theodore Roosevelt Federal Building headquarters of the U.S. Office of Personnel...",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Kevin Dietsch/Getty Images",
          "id": "67a17491c13704014688fa49",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_1024,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg",
              "srcset": "https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_120,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 120w, https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_240,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 240w, https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_320,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 320w, https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_640,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 640w, https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_960,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_1280,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg",
              "srcset": "https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_120,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 120w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_240,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 240w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_320,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 320w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_640,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 640w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_960,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 960w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_1280,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_1280,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg",
              "srcset": "https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_120,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 120w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_240,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 240w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_320,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 320w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_640,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 640w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_960,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 960w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_1280,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_1024,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg",
              "srcset": "https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_120,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 120w, https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_240,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 240w, https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_320,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 320w, https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_640,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 640w, https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_960,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_1280,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg",
              "srcset": "https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_120,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 120w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_240,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 240w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_320,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 320w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_640,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 640w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_960,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 960w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_1280,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 1280w"
            }
          },
          "masterAspectRatio": "2000:1326",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_1024,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg",
                "srcset": "https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_120,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 120w, https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_240,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 240w, https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_320,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 320w, https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_640,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 640w, https://media.wired.com/photos/67a17491c13704014688fa49/16:9/w_960,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_1280,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg",
                "srcset": "https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_120,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 120w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_240,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 240w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_320,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 320w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_640,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 640w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_960,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 960w, https://media.wired.com/photos/67a17491c13704014688fa49/3:2/w_1280,c_limit/DOGE-Restraining-Order-Politics-2197495858.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "DOGE"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "Federal Workers Sue to Disconnect DOGE Server",
          "dek": "Two federal workers, citing reports that Elon Musk’s associates are operating an illegally connected email server at OPM, seek a restraining order."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/federal-workers-sue-over-doge-server/",
        "functionalTags": []
      },
      {
        "id": "67a1fd32afca9e5e2c6e2456",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/carlton-reid/\">Carlton Reid</a> is an award-winning freelancer who writes about cycling, transport and adventure travel for numerous titles including Forbes, The Guardian, and Mail Online. He is the author of <em>Roads Were Not Built for Cars</em> and <em>Bike Boom.</em> ... <a href=\"/author/carlton-reid\">Read more</a>",
                "dangerousTitle": null,
                "name": "Carlton Reid",
                "socialMedia": [],
                "url": "/author/carlton-reid/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "67a1fd32afca9e5e2c6e2456",
        "dangerousHed": "Trump&#39;s Plan to Make European Cars More Expensive Has a Fatal Flaw",
        "dangerousDek": "President Trump&#39;s threat of 25 percent tariffs on EU car imports could spark an automotive trade war&#8212;one that will result in higher prices for all and never end in European consumers buying more American autos.",
        "date": "02.04.2025",
        "pubDate": "2025-02-04T14:42:36.561Z",
        "issueDate": "",
        "image": {
          "altText": "Search",
          "caption": "",
          "contentType": "photo",
          "credit": "Photo-Illustration: Wired Staff; Ford/Getty Images",
          "id": "67a23aec71b4a5f3a9086488",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_1024,c_limit/truck-eu-gear.jpg",
              "srcset": "https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_120,c_limit/truck-eu-gear.jpg 120w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_240,c_limit/truck-eu-gear.jpg 240w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_320,c_limit/truck-eu-gear.jpg 320w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_640,c_limit/truck-eu-gear.jpg 640w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_960,c_limit/truck-eu-gear.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_1280,c_limit/truck-eu-gear.jpg",
              "srcset": "https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_120,c_limit/truck-eu-gear.jpg 120w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_240,c_limit/truck-eu-gear.jpg 240w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_320,c_limit/truck-eu-gear.jpg 320w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_640,c_limit/truck-eu-gear.jpg 640w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_960,c_limit/truck-eu-gear.jpg 960w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_1280,c_limit/truck-eu-gear.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_1280,c_limit/truck-eu-gear.jpg",
              "srcset": "https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_120,c_limit/truck-eu-gear.jpg 120w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_240,c_limit/truck-eu-gear.jpg 240w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_320,c_limit/truck-eu-gear.jpg 320w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_640,c_limit/truck-eu-gear.jpg 640w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_960,c_limit/truck-eu-gear.jpg 960w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_1280,c_limit/truck-eu-gear.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_1024,c_limit/truck-eu-gear.jpg",
              "srcset": "https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_120,c_limit/truck-eu-gear.jpg 120w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_240,c_limit/truck-eu-gear.jpg 240w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_320,c_limit/truck-eu-gear.jpg 320w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_640,c_limit/truck-eu-gear.jpg 640w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_960,c_limit/truck-eu-gear.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_1280,c_limit/truck-eu-gear.jpg",
              "srcset": "https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_120,c_limit/truck-eu-gear.jpg 120w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_240,c_limit/truck-eu-gear.jpg 240w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_320,c_limit/truck-eu-gear.jpg 320w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_640,c_limit/truck-eu-gear.jpg 640w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_960,c_limit/truck-eu-gear.jpg 960w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_1280,c_limit/truck-eu-gear.jpg 1280w"
            }
          },
          "masterAspectRatio": "2400:1350",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_1024,c_limit/truck-eu-gear.jpg",
                "srcset": "https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_120,c_limit/truck-eu-gear.jpg 120w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_240,c_limit/truck-eu-gear.jpg 240w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_320,c_limit/truck-eu-gear.jpg 320w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_640,c_limit/truck-eu-gear.jpg 640w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/16:9/w_960,c_limit/truck-eu-gear.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_1280,c_limit/truck-eu-gear.jpg",
                "srcset": "https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_120,c_limit/truck-eu-gear.jpg 120w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_240,c_limit/truck-eu-gear.jpg 240w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_320,c_limit/truck-eu-gear.jpg 320w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_640,c_limit/truck-eu-gear.jpg 640w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_960,c_limit/truck-eu-gear.jpg 960w, https://media.wired.com/photos/67a23aec71b4a5f3a9086488/3:2/w_1280,c_limit/truck-eu-gear.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Size Matters"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "Trump's Plan to Make European Cars More Expensive Has a Fatal Flaw",
          "dek": "President Trump’s threat of 25 percent tariffs on EU car imports could spark an automotive trade war—one that will result in higher prices for all and will never end in European consumers buying more American autos."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/trumps-plan-to-make-european-cars-more-expensive-has-a-fatal-flaw/",
        "functionalTags": []
      },
      {
        "id": "67995c705d8a4b315c00c2ed",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/boutayna-chokrane/\">Boutayna Chokrane </a>is a product writer and reviewer at WIRED. Before joining the Gear team, she was a music editorial fellow at Pitchfork. She also worked as a freelance journalist, covering fashion, art, and culture for Vogue, Rolling Stone, the Cut, and others. She graduated from Northwestern University with a ... <a href=\"/author/boutayna-chokrane\">Read more</a>",
                "dangerousTitle": "Product Writer &amp; Reviewer",
                "name": "Boutayna Chokrane ",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/671bf33caf7e5d470fafdb55/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [],
                "url": "/author/boutayna-chokrane/"
              }
            ]
          }
        },
        "contentType": "gallery",
        "copilotID": "67995c705d8a4b315c00c2ed",
        "dangerousHed": "Best Gifts for Women Who’ve Checked Out of Planet Earth",
        "dangerousDek": "She’s seen enough. She’s had enough. She can’t book a one-way ticket to the stars (yet), but these gifts will help her transcend this world.",
        "date": "02.04.2025",
        "pubDate": "2025-02-04T14:41:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "Lego galaxy set sleep mask hair dryer and metallic reusable waterbottle. Background pink watercolor texture.",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Lego; Therabody; Larq; Ulta; Getty Images",
          "id": "67a18bd0be210d10079b54e5",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_1024,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg",
              "srcset": "https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_120,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 120w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_240,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 240w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_320,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 320w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_640,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 640w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_960,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_1280,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg",
              "srcset": "https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_120,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 120w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_240,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 240w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_320,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 320w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_640,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 640w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_960,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 960w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_1280,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_1280,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg",
              "srcset": "https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_120,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 120w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_240,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 240w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_320,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 320w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_640,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 640w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_960,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 960w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_1280,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_1024,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg",
              "srcset": "https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_120,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 120w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_240,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 240w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_320,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 320w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_640,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 640w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_960,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_1280,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg",
              "srcset": "https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_120,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 120w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_240,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 240w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_320,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 320w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_640,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 640w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_960,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 960w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_1280,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 1280w"
            }
          },
          "masterAspectRatio": "2000:1300",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_1024,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg",
                "srcset": "https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_120,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 120w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_240,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 240w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_320,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 320w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_640,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 640w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/16:9/w_960,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_1280,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg",
                "srcset": "https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_120,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 120w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_240,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 240w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_320,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 320w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_640,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 640w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_960,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 960w, https://media.wired.com/photos/67a18bd0be210d10079b54e5/3:2/w_1280,c_limit/Gift%20Guide%20for%20Women%20Abstract%20Background%20022025%20SOURCE%20Lego%20Therabody%20Larq%20Ulta.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "itemsCount": {
          "count": 10,
          "itemType": "slide"
        },
        "rubric": {
          "name": "Universal Unsubscribe"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "Best Gifts for Women Who’ve Checked Out of Planet Earth",
          "dek": "She’s seen enough. She’s had enough. She can’t book a one-way ticket to the stars (yet), but these gifts will help her transcend this world."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/gallery/gifts-for-women-who-are-over-this-planet/",
        "functionalTags": []
      },
      {
        "id": "679d402e15561df7f22f99ca",
        "contributors": {
          "author": {
            "items": [
              {
                "dangerousBio": "<a href=\"/author/steven-levy/\">Steven Levy</a> covers the gamut of tech subjects for WIRED, in print and online, and has been contributing to the magazine since its inception. His weekly column, <a href=\"https://www.wired.com/newsletter/plaintext?sourceCode=AuthorBio\">Plaintext</a>, is exclusive to subscribers online but the newsletter version is open to all&#8212;<a href=\"https://www.wired.com/newsletter/plaintext?sourceCode=AuthorBio\"><strong>sign up here</strong></a>. He has been writing about technology for ... <a href=\"/author/steven-levy\">Read more</a>",
                "dangerousTitle": "Editor at Large",
                "name": "Steven Levy",
                "photo": {
                  "altText": "",
                  "sources": {
                    "sm": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_960,c_limit/undefined 960w"
                    },
                    "lg": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "xxl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_1280,c_limit/undefined 1280w"
                    },
                    "md": {
                      "aspectRatio": "16:9",
                      "width": 1024,
                      "url": "https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_1024,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_960,c_limit/undefined 960w"
                    },
                    "xl": {
                      "aspectRatio": "3:2",
                      "width": 1280,
                      "url": "https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_1280,c_limit/undefined",
                      "srcset": "https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_1280,c_limit/undefined 1280w"
                    }
                  },
                  "segmentedSources": {
                    "sm": [
                      {
                        "aspectRatio": "16:9",
                        "width": 1024,
                        "url": "https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_1024,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/16:9/w_960,c_limit/undefined 960w"
                      }
                    ],
                    "lg": [
                      {
                        "aspectRatio": "3:2",
                        "width": 1280,
                        "url": "https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_1280,c_limit/undefined",
                        "srcset": "https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_120,c_limit/undefined 120w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_240,c_limit/undefined 240w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_320,c_limit/undefined 320w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_640,c_limit/undefined 640w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_960,c_limit/undefined 960w, https://media.wired.com/photos/65e83761c9d1003a19b2989e/3:2/w_1280,c_limit/undefined 1280w"
                      }
                    ]
                  }
                },
                "socialMedia": [
                  {
                    "handle": "StevenLevy",
                    "network": "twitter",
                    "label": "Follow Steven Levy on X"
                  }
                ],
                "url": "/author/steven-levy/"
              }
            ]
          }
        },
        "contentType": "article",
        "copilotID": "679d402e15561df7f22f99ca",
        "dangerousHed": "Chris Anderson Is Giving TED Away to Whoever Has the Best Idea for Its Future",
        "dangerousDek": "In an exclusive interview with WIRED, the British entrepreneur shares why it’s time to move on from TED.",
        "date": "02.04.2025",
        "pubDate": "2025-02-04T14:00:00.000Z",
        "issueDate": "",
        "image": {
          "altText": "16 January 2025 Bavaria Munich Chris Anderson TED Conferences will be speaking on stage at the Digital Life Design ...",
          "caption": "",
          "contentType": "photo",
          "credit": "Photograph: Matthias Balk/Getty Images",
          "id": "679d446409ea0df62c1a1cbd",
          "sources": {
            "sm": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_1024,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg",
              "srcset": "https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_120,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 120w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_240,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 240w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_320,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 320w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_640,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 640w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_960,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 960w"
            },
            "lg": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_1280,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg",
              "srcset": "https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_120,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 120w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_240,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 240w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_320,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 320w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_640,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 640w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_960,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 960w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_1280,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 1280w"
            },
            "xxl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_1280,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg",
              "srcset": "https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_120,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 120w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_240,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 240w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_320,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 320w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_640,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 640w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_960,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 960w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_1280,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 1280w"
            },
            "md": {
              "aspectRatio": "16:9",
              "width": 1024,
              "url": "https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_1024,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg",
              "srcset": "https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_120,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 120w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_240,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 240w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_320,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 320w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_640,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 640w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_960,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 960w"
            },
            "xl": {
              "aspectRatio": "3:2",
              "width": 1280,
              "url": "https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_1280,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg",
              "srcset": "https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_120,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 120w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_240,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 240w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_320,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 320w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_640,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 640w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_960,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 960w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_1280,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 1280w"
            }
          },
          "masterAspectRatio": "2000:1334",
          "segmentedSources": {
            "sm": [
              {
                "aspectRatio": "16:9",
                "width": 1024,
                "url": "https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_1024,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg",
                "srcset": "https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_120,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 120w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_240,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 240w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_320,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 320w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_640,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 640w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/16:9/w_960,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 960w"
              }
            ],
            "lg": [
              {
                "aspectRatio": "3:2",
                "width": 1280,
                "url": "https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_1280,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg",
                "srcset": "https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_120,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 120w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_240,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 240w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_320,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 320w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_640,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 640w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_960,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 960w, https://media.wired.com/photos/679d446409ea0df62c1a1cbd/3:2/w_1280,c_limit/Chris-Anderson-TED-Stepping-Down-Business-2193767794.jpg 1280w"
              }
            ]
          }
        },
        "imageLabels": [],
        "isSponsored": false,
        "rubric": {
          "name": "Bright Idea"
        },
        "signage": null,
        "hasNoFollowOnSyndicated": false,
        "source": {
          "hed": "Chris Anderson Is Giving TED Away to Whoever Has the Best Idea for Its Future",
          "dek": "In an exclusive interview with WIRED, the British entrepreneur shares why it’s time to move on from TED."
        },
        "showAssetOnly": false,
        "showLinkedAsset": false,
        "url": "/story/chris-anderson-steps-down-ted/",
        "functionalTags": []
      }
    ],
    "nextPageURL": "/search/?q=&page=3",
    "pageSize": 8,
    "resultCount": 10000,
    "searchTerm": "",
    "searchHeading": "",
    "hasTwoLinedHeader": false,
    "sort": {
      "value": "score desc",
      "label": "Relevance"
    },
    "sortOptions": [
      {
        "value": "publishdate desc",
        "label": "Newest"
      },
      {
        "value": "score desc",
        "label": "Relevance"
      }
    ],
    "summaryItemVariation": "SideBySideDesktopOnly",
    "totalPageCount": 1250,
    "hasFilterBar": false
  },
  "layoutConfigs": {},
  "featureFlags": {
    "shouldUseBookmarkV3": true,
    "enableAggressiveNewsletter": false,
    "enableEntitlementProxy": true,
    "enableEntitlementValidation": false,
    "enableGqlForLinkBanner": true,
    "enableLinkStack": true,
    "enableRecipeRatings": false,
    "enableSlimNewsletter": false,
    "enableTrendingStoriesFromCopilot": true,
    "enableUserContext": true,
    "shouldKeepSubscribeLinkActive": true,
    "recentWorkTeaser": "channel-only",
    "bundleTeaser": "rubric-only",
    "contentTeaser": "channel-only",
    "tagTeaser": "channel-only",
    "preferCollectionGrid": false,
    "overrideBodyContentHeadings": true,
    "shouldTransformDashes": true,
    "rubricParentSlug": "category",
    "usePrimaryCategoryAsRubric": true,
    "leadInWordCount": 3,
    "enableSponsoredContentInRelated": false,
    "personalizeRecircMostPopular": true,
    "videoPersistable": false,
    "google": {
      "swgEnabled": true,
      "signInEnabled": true
    },
    "featureOnboarding": {
      "bookmarks": true
    },
    "pageSize": 24,
    "searchPageDateFormat": "MM.DD.YYYY",
    "shouldUseUppercaseHead": true,
    "useSearchRendition": true,
    "enableAccounts": true,
    "enableActionBar": true,
    "enableBookmarking": false,
    "enableConsent": true,
    "enableDropcap": false,
    "enableInfinityId": true,
    "enableJourneyPayment": false,
    "enableMediaOverridesV2": true,
    "personalizeRecircList": true
  }
}
```
</details>

<https://www.wired.com/most-recent/> tops out on page 500 (also has an API if you add `format=json` to the query parameters). Earliest article is May 2nd 2022.
## The Verge

Has an archive page that goes back to 2011 <https://www.theverge.com/archives/2025/1/1>   

## Mashable

The API the main page uses to load more articles (`/?ajax=1&page=4000`) doesn't seem to have any limits in terms of how far back it will go. It returns the articles as HTML.