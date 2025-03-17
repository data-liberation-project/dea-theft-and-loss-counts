#  Data: Theft/Loss of Controlled Substances

This repository contains [spreadsheets](data/raw/) from the US Drug Enforcement Administration (DEA), counting the number of controlled substance (and regulated chemical) thefts/losses reported to the agency — by state, business activity, loss type, and year — plus the overall quantities stolen/lost.

The spreadsheets were obtained in May 2023 via a [Freedom of Information Act (FOIA) request](https://www.data-liberation-project.org/requests/controlled-substance-theft-and-loss/) submitted by the [Data Liberation Project](https://www.data-liberation-project.org/). The DLP also obtained a [manual, partially redacted,](https://www.documentcloud.org/documents/25589722-dea-theftloss-of-controlled-substances-manual-partially-redacted/) describing how to fill out the TLR program.

This repository also contains [“tidy” CSV representations](data/tidy/) of the same data, plus the [Python code](scripts/convert-to-csv.py) used for the conversion.

## Background

The DEA [requires](https://www.deadiversion.usdoj.gov/21cfr_reports/theft/index.html) all entities it has authorized to manufacture or handle [controlled substances](https://www.deadiversion.usdoj.gov/schedules/) and “[listed chemicals](https://www.deadiversion.usdoj.gov/chem_prog/34chems.htm)” to inform the agency about any “theft or significant loss of any controlled substance, disposal receptacles or listed chemicals within one business day of discovery of such loss or theft.”

Those reports are collected via the DEA’s [Theft Loss Reporting (TLR) system](https://apps.deadiversion.usdoj.gov/TLR/), which allows registrants to submit the following forms electronically:

- [Form DEA-106](https://deadiversion.usdoj.gov/21cfr_reports/theft/DEA_Form_106.pdf), “Report of Theft or Loss of Controlled Substances,” [OMB Control No. 1117-0001](https://www.reginfo.gov/public/do/PRAOMBHistory?ombControlNumber=1117-0001)
- [Form DEA-107](https://www.reginfo.gov/public/do/DownloadDocument?objectID=103735201), “Report of Theft or Loss of Listed Chemical,” [OMB Control No. 1117-0024](https://www.reginfo.gov/public/do/PRAOMBHistory?ombControlNumber=1117-0024)

The Data Liberation Project’s [FOIA request](https://www.documentcloud.org/documents/22925202-2022-09-23-dojdea-tlr-foia-request), submitted in September 2022, sought database records collected through the TLR system, Form DEA-106, and Form DEA-107 (excluding narrative data fields and data fields that contain personal information about individual persons), plus all relevant database documentation.

## Spreadsheets provided by the DEA

In May 2023, the DEA sent its response to the Data Liberation Project. Along with its [determination letter](https://www.documentcloud.org/documents/23813617-2023-05-12-signed-det-65), the agency provided two spreadsheets, which you can [download here](data/raw/). (The agency did not provide any of the underlying report data requested.)

The spreadsheets contain two sets of analogous statistical reports, one for __controlled substances__ (302,547 incidents from 2010 to Sept. 2022) and the other for __listed chemicals__ (756 incidents from 2019 to Sept. 2022). Each spreadsheet contains the following sub-sheets:

- `TLR Disclaimer`: A disclaimer about the data; see below.
- `Glossary`: A table defining the key terms in the spreadsheet.
- `Theft by Bus Act-Loss Type`: A report counting the number of thefts by “business activity” (see below), “loss type” (see below), and year (see below).
- `Theft by Loss Type-Bus Act`: The same report, but with a different ordering of the subtotals.
- `No of Thefts by State-Bus Act`: A report counting the number of thefts by state, business activity, and year.
- `No of Thefts by State-Loss Type`: A report counting the number of thefts by state, business activity, and year.
- `Total Quantity Lost by State`: A report counting the total quantity of substance/chemical lost, by state, business activity, loss type, and unit of measurement (either gram, milligram, milliliter, or unit).


### DEA disclaimer

*The text below comes directly from the spreadsheets.*

> NOTE:  DEA’s Theft/Loss Report (TLR) is a collection of information reported by registrants under the regulatory requirement to report thefts and losses of controlled substances (21 C.F.R. §§ 1301.74 and 1301.76).  Registrants are not required to report the ultimate recovery of these drugs.  The systems and requirements also do not capture disposal of controlled substances.

> CAUTION should be exercised in drawing conclusions from this data.

> The information contained in TLR generated reports is a complete and accurate record of what DEA registrants reported to the TLR reporting sytem, via the electronic DEA form 106, in accordance with reporting requirements.  This information is susceptible to future updates and corrections, without notice, as new information is obtained.  Recipients should be aware of these limitations before analyzing or publishing DTL data.  DEA assumes no liability for analysis, conclusions or policy decisions of third parties based on internal interpretation of the provided data.

> A reported theft or loss does not necessarily equate to illicit use.

> In the TLR database, when a single incident involves the theft of multiple drugs, e.g., hydrocodone and oxycodone; each drug is reported as an individual theft.  As a result, when data is sorted by drug, instead of number of incidents (occurences), caution should be used, as the total number of thefts will appear to be higher.  Also, TLR totals will fluctuate if corrections, updates, or hardcopy DEA 106 forms are submitted after-the-fact. 

### DEA glossary

*The table below comes directly from the spreadsheets.*

| Header | Description |
|--------|-------------|
| BUSINESS ACTIVITY | Reporting Registrant’s Business |
| LOSS TYPE | Describes the different types of losses. (Break-in/Burglary, Customer Theft (or Non Employee), Disaster (Fire, Weather, Etc.), Employee Theft (Or Suspected), Hijacking Of Transport Vehicle, Loss in Transit, Other, Packaging Discrepancy and Robbery |
| STATE | Location for the reported theft/loss |
| UNIT OF MEASURE | Describes the dosage form for the drug(s) reported lost (Unit, Milliliter, Grams or milligram) |
| NUMBER OF THEFTS | Represents number of individual thefts reported |
| TOTAL QUANTITY LOST | Equals total amount of drugs reported lost |

### “Business activity”

The DEA uses the following categories for “business activity,” presented here in alphabetical order:

- `ANALYTICAL LAB`
- `CANINE HANDLER`
- `DISTRIBUTOR`
- `EXPORTER`
- `HOSPITAL`
- `IMPORTER`
- `MANUFACTURER`
- `MID LEVEL PRACTITIONER`
- `NTP` (i.e., Narcotic Treatment Program)
- `PHARMACY`
- `PRACTITIONER`
- `RESEARCHER`
- `REVERSE DISTRIBUTOR`
- `TEACHING INSTITUTION`

### “Loss type”

The DEA uses the following categories for “loss type,” presented here in alphabetical order:

- `BREAK-IN/BURGLARY`
- `CUSTOMER THEFT (OR NON EMPLOYEE)`
- `DISASTER (FIRE, WEATHER, ETC.)`
- `EMPLOYEE THEFT (OR SUSPECTED)`
- `HIJACKING OF TRANSPORT VEHICLE`
- `LOSS IN TRANSIT`
- `OTHER`
- `PACKAGING DISCREPANCY`
- `ROBBERY`

### Years covered

The data covers a longer timespan for controlled substances than for the listed chemicals:

- Controlled substances: 2010–2021, plus “JAN-SEP 2022”
- Listed chemicals: 2019–2021, plus “JAN-SEP 2022”

## “Tidy” CSV files

Depending on your toolset, the format and structure of the DEA’s spreadsheets might not be ideal for performing further analysis. For instance:

- They use implicit values in the categorical columns, where blanks indicate *same category as above*
- They include subtotals, which can cause problems with double-counting if not careful
- They arrange the data in a “wide” format, where each year is its own column

For those who prefer “[tidy](https://vita.had.co.nz/papers/tidy-data.html)” data and/or the CSV file format, the Data Liberation Project has converted the original spreadsheets into a [__series of CSV files__](data/tidy), which represent each of the aggregations available in the raw data.

### Notes on the conversion

- `csub-` files represent the controlled substances data, while `chem-` files represent the chemicals data.
- All subtotals (by category and year) and grand totals in the spreadsheets have been removed, to avoid accidental double-counting.
- The “Loss Type” values were all-caps in the controlled substances spreadsheet but title-cased in the chemicals spreadsheet. The tidy CSV files use all-caps for both.
- Please see the full notes (including the DEA disclaimer) on the spreadsheets in the main section above.

The Python code used to generate the CSV files can be viewed [here](scripts/convert-to-csv.py).

## Licensing

The original DEA spreadsheets are, as government documents, now in the public domain. The Data Liberation Project–generated [CSV files](data/tidy/) are available under Creative Commons’ [CC BY-SA 4.0 license terms](https://creativecommons.org/licenses/by-sa/4.0/). This repository’s code is available under the [MIT License terms](https://opensource.org/license/mit/). 
