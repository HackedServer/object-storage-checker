# object-storage-checker

Uses https://github.com/jsdelivr/globalping probes to monitor a list of storage objects across various service providers.

Focus is on S3 compatiable providers.

In time this script will log this data and have graphs, etc.

## Curent Monitored List

<!-- BEGIN-GENERATION -->

## Amazon - Amazon Web Services - S3
| Country | Continent | City, State | Region | S3 Endpoint |
|---|---|---|---|---|
| US | NA | Oregon | us-west-2 | https://s3.dualstack.us-west-2.amazonaws.com |
| US | NA | Virginia | us-east-1 | https://s3.dualstack.us-east-1.amazonaws.com |
| US | NA | California | us-west-1 | https://s3.dualstack.us-west-1.amazonaws.com |
| US | NA | Ohio | us-east-2 | https://s3.dualstack.us-east-2.amazonaws.com |
| BR | SA | Sao Paolo | sa-east-1 | https://s3.dualstack.sa-east-1.amazonaws.com |
| SE | EU | Stockholm | eu-north-1 | https://s3.dualstack.eu-north-1.amazonaws.com |
| FR | EU | Paris | eu-west-3 | https://s3.dualstack.eu-west-3.amazonaws.com |
| UK | EU | London | eu-west-2 | https://s3.dualstack.eu-west-2.amazonaws.com |
| IN | AS | Mumbai | ap-south-1 | https://s3.dualstack.ap-south-1.amazonaws.com |
| JP | AS | Osaka | ap-northeast-3 | https://s3.dualstack.ap-northeast-3.amazonaws.com |
| KR | AS | Seoul | ap-northeast-2 | https://s3.dualstack.ap-northeast-2.amazonaws.com |
| SG | AS | Singapore | ap-southeast-1 | https://s3.dualstack.ap-southeast-1.amazonaws.com |
| AU | OC | Sydney | ap-southeast-2 | https://s3.dualstack.ap-southeast-2.amazonaws.com |
| JP | AS | Tokyo | ap-northeast-1 | https://s3.dualstack.ap-northeast-1.amazonaws.com |
| IE | EU | Dublin | eu-west-1 | https://s3.dualstack.eu-west-1.amazonaws.com |
| DE | EU | Frankfurt | eu-central-1 | https://s3.dualstack.eu-central-1.amazonaws.com |
| CA | NA | Montreal | ca-central-1 | https://s3.dualstack.ca-central-1.amazonaws.com |

## Microsoft - Azure - Blob Storage
| Country | Continent | City, State | Region | S3 Endpoint |
|---|---|---|---|---|
| SE | EU |  | sweden | :question: |

## Backblaze - Backblaze - B2
| Country | Continent | City, State | Region | S3 Endpoint |
|---|---|---|---|---|
| US | NA |  | us-west-001 | https://s3.us-west-001.backblazeb2.com |
| NL | EU | Amsterdam | eu-central-003 | https://s3.eu-central-003.backblazeb2.com |

## Cloudflare - Cloudflare - R2
| Country | Continent | City, State | Region | S3 Endpoint |
|---|---|---|---|---|
| Global | NA |  | auto | https://634d2993234c9eeb2905ddb98de372e5.r2.cloudflarestorage.com |

## iDrive - iDrive - e2
| Country | Continent | City, State | Region | S3 Endpoint |
|---|---|---|---|---|
| US | NA | Chicago, Illinois | us-ch | https://s9h3.ch12.idrivee2-15.com |
| US | NA | Dallas, Texas | us-da | https://b6d6.da12.idrivee2-14.com |
| IE | EU |  | eu-ie | https://e6y1.ie11.idrivee2-6.com |
| US | NA | Los Angeles, California | us-la | https://b2w8.la12.idrivee2-14.com |
| US | NA | Miami, Florida | us-mi | https://t2l6.mi12.idrivee2-13.com |
| US | NA | Oregon | us-or | https://i1f1.or12.idrivee2-12.com |
| US | NA | Phoenix, Arizona | us-ph | https://x0i8.ph11.idrivee2-11.com |
| US | NA | San Jose, California | us-sj | https://g9u6.sj11.idrivee2-10.com |
| US | NA | Virginia | us-va | https://g7o1.va12.idrivee2-9.com |

## Oracle - Oracle Cloud - Object Storage
| Country | Continent | City, State | Region | S3 Endpoint |
|---|---|---|---|---|
| US | NA | San Jose, California | us-sanjose-1 | https://axav54powbko.compat.objectstorage.us-sanjose-1.oraclecloud.com |
| DE | EU | Frankfurt | eu-frankfurt-1 | https://axav54powbko.compat.objectstorage.eu-frankfurt-1.oraclecloud.com |
| US | NA | Phoenix, Arizona | us-phoenix-1 | https://axav54powbko.compat.objectstorage.us-phoenix-1.oraclecloud.com |
| UK | EU | Newport | uk-cardiff-1 | https://axav54powbko.compat.objectstorage.uk-cardiff-1.oraclecloud.com |

## Scaleway - Scaleway - Object Storage
| Country | Continent | City, State | Region | S3 Endpoint |
|---|---|---|---|---|
| FR | EU | Paris | fr-par | https://s3.fr-par.scw.cloud |
| NL | EU | Amsterdam | nl-ams | https://s3.nl-ams.scw.cloud |
| PL | EU | Warsaw | pl-waw | https://s3.pl-waw.scw.cloud |

## Synology - C2 - Object Storage
| Country | Continent | City, State | Region | S3 Endpoint |
|---|---|---|---|---|
| DE | EU | Frankfurt | eu-001 | https://eu-001.s3.synologyc2.net |
| US | NA | Seattle | us-001 | https://us-001.s3.synologyc2.net |
| TW | AS |  | tw-001 | https://tw-001.s3.synologyc2.net |

## Wasabi - Wasabi - Cloud Storage
| Country | Continent | City, State | Region | S3 Endpoint |
|---|---|---|---|---|
| US | NA | Oregon | us-west-1 | https://s3.us-west-1.wasabisys.com |
| US | NA | Virginia | us-east-1 | https://s3.us-east-1.wasabisys.com |
| US | NA | Virginia | us-east-2 | https://s3.us-east-2.wasabisys.com |
| US | NA | Texas | us-central-1 | https://s3.us-central-1.wasabisys.com |
| NL | EU | Amserdam | eu-central-1 | https://s3.eu-central-1.wasabisys.com |
| CA | NA | Toronto | ca-central-1 | https://s3.ca-central-1.wasabisys.com |
| DE | EU | Frankfurt | eu-central-2 | https://s3.eu-central-2.wasabisys.com |
| UK | EU | London | eu-west-1 | https://s3.eu-west-1.wasabisys.com |
| FR | EU | Paris | eu-west-2 | https://s3.eu-west-2.wasabisys.com |
| JP | AS | Tokyo | ap-northeast-1 | https://s3.ap-northeast-1.wasabisys.com |
| JP | AS | Osaka | ap-northeast-2 | https://s3.ap-northeast-2.wasabisys.com |
| SG | AS | Singapore | ap-southeast-1 | https://s3.ap-southeast-1.wasabisys.com |
| AU | AS | Sydney | ap-southeast-2 | https://s3.ap-southeast-2.wasabisys.com |
