{% docs yellow_trips_vendorid_desc %}

A code indicating the TPEP provider (the technology system vendor in the taxi) that provided the record.

| Code | Provider                          |
|------|-----------------------------------|
| 1    | Creative Mobile Technologies, LLC |
| 2    | Curb Mobility, LLC                |
| 6    | Myle Technologies Inc             |
| 7    | Helix                             |

{% enddocs %}

{% docs yellow_trips_ratecodeid_desc %}

The final rate code in effect at the end of the trip.

| Code | Description           |
|------|-----------------------|
| 1    | Standard rate         |
| 2    | JFK                   |
| 3    | Newark                |
| 4    | Nassau or Westchester |
| 5    | Negotiated fare       |
| 6    | Group ride            |
| 99   | Null/unknown          |

{% enddocs %}

{% docs yellow_trips_store_and_fwd_flag_desc %}
    
Indicates if the trip record was held locally ('stored') in the vehicle's memory before being uploaded ('forwarded') to the vendor's server due to a temporary lack of network connectivity.

| Flag | Meaning                       |
|------|-------------------------------|
| Y    | Store and forward trip        |
| N    | Not a store and forward trip  |
| Null | (Potentially, if applicable)  |

{% enddocs %}

{% docs yellow_trips_payment_type_desc %}

A numeric code signifying how the passenger paid for the trip.

| Code | Description   | Notes                                                             |
|------|---------------|-------------------------------------------------------------------|
| 0    | Flex Fare trip| Check TLC documentation for current definition.                   |
| 1    | Credit card   |                                                                   |
| 2    | Cash          |                                                                   |
| 3    | No charge     | Trip with zero fare (e.g., promotional, driver testing)           |
| 4    | Dispute       | Fare disputed by passenger.                                       |
| 5    | Unknown       | Payment method could not be determined.                           |
| 6    | Voided trip   | Trip cancelled or invalidated after meter engagement.             |

{% enddocs %}