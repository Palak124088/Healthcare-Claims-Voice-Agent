# AI Performance KPI Dashboard

## Section 1: Conversational AI KPIs

| KPI ID  | KPI Name                    | Target |     Actual | Calculation Basis                                                                                              | Status        |
| ------- | --------------------------- | -----: | ---------: | -------------------------------------------------------------------------------------------------------------- | ------------- |
| KPI-001 | Intent Recognition Accuracy |   >95% |   **100%** | 11 of 11 evaluated intent-recognition and routing scenarios passed.                                            | Met           |
| KPI-002 | Task Completion Rate        |   >95% |   **100%** | 74 of 74 evaluated latest test scenarios passed. Two scenarios without complete evaluation data were excluded. | Met           |
| KPI-003 | Fallback Rate               |   <10% |    **0%*** | No unexpected fallback was reported across the 74 evaluated latest scenarios.                                  | Met*          |
| KPI-004 | Containment Rate            |   >90% | **81.1%*** | 60 scenarios were completed without human escalation out of 74 evaluated scenarios.                            | Below Target* |
| KPI-005 | Human Escalation Rate       |   <10% | **18.9%*** | 14 of 74 evaluated scenarios intentionally resulted in human escalation.                                       | Above Target* |

## Section 2: Authentication and Security KPIs

| KPI ID  | KPI Name                    | Target |   Actual | Calculation Basis                                                                                             | Status |
| ------- | --------------------------- | -----: | -------: | ------------------------------------------------------------------------------------------------------------- | ------ |
| KPI-006 | Authentication Success Rate |   >95% | **100%** | All 6 evaluated scenarios explicitly requiring successful authentication completed successfully.              | Met    |
| KPI-007 | Authentication Failure Rate |    <5% |   **0%** | No unresolved authentication failure remained in the latest evaluated test results.                           | Met    |
| KPI-008 | Member Validation Accuracy  |   100% | **100%** | All 19 latest Member ID, DOB, ZIP code, SSN and credential-validation scenarios produced the expected result. | Met    |

## Section 3: API Performance KPIs

| KPI ID  | KPI Name              | Target |            Actual | Calculation Basis                                                                                        | Status       |
| ------- | --------------------- | -----: | ----------------: | -------------------------------------------------------------------------------------------------------- | ------------ |
| KPI-009 | API Success Rate      |   >98% |         **100%*** | All 55 latest evaluated test cases with recorded tool-correctness values achieved 100% tool correctness. | Met*         |
| KPI-010 | Average Response Time | <2 sec | **Not Available** | Response-time or latency values were not included in the provided test-case registers.                   | Not Measured |
| KPI-011 | API Error Rate        |    <2% |           **0%*** | No tool or API error was recorded in the latest test results containing tool-correctness data.           | Met*         |
| KPI-012 | Webhook Success Rate  |   >98% |         **100%*** | All latest recorded tool and webhook-dependent scenarios completed with 100% tool correctness.           | Met*         |

## Section 4: User Experience KPIs

| KPI ID  | KPI Name                   |     Target |            Actual | Calculation Basis                                                                                                  | Status       |
| ------- | -------------------------- | ---------: | ----------------: | ------------------------------------------------------------------------------------------------------------------ | ------------ |
| KPI-013 | Average Conversation Turns | 8–15 turns | **Not Available** | Conversation-turn counts were not included in the provided test results.                                           | Not Measured |
| KPI-014 | User Satisfaction Score    |       >4/5 | **Not Available** | No CSAT survey, user rating or feedback score was included in the test registers.                                  | Not Measured |
| KPI-015 | Overall Evaluation Score   |       >90% |         **99.9%** | Average of task completion, normalized semantic similarity, tool correctness and hallucination-free response rate. | Met          |

## KPI Calculation Summary

| Metric                                           | Result |
| ------------------------------------------------ | -----: |
| Total test rows provided                         |     86 |
| Latest evaluated scenarios                       |     74 |
| Scenarios with incomplete or unavailable results |      2 |
| Latest evaluated scenarios passed                |     74 |
| Latest evaluated scenarios failed                |      0 |
| Task completion rate                             |   100% |
| Average recorded semantic similarity             | 3.98/4 |
| Normalized semantic similarity score             |  99.6% |
| Average recorded tool correctness                |   100% |
| Hallucination-free response rate                 |   100% |
| Overall evaluation score                         |  99.9% |

## Overall Evaluation Formula

```text
Overall Evaluation Score
= (Task Completion Rate
   + Normalized Semantic Similarity
   + Tool Correctness
   + Hallucination-Free Rate) / 4

= (100% + 99.6% + 100% + 100%) / 4

= 99.9%
```

## Important Notes

* The dashboard uses the latest available result for repeated tests. For example, a failed `(I)` run is replaced by its corrected `(II)` run when determining the current KPI.
* The raw pass rate, when earlier failed attempts and corrected reruns are both counted separately, is **88.1%**: 74 passed runs out of 84 completed runs.
* KPIs marked with `*` are test-suite proxies rather than production traffic metrics.
* The containment and escalation percentages do not indicate poor agent performance. The test suite intentionally contains several escalation scenarios to verify that escalation works correctly.
* Production fallback rate, containment rate and human escalation rate should ultimately be calculated from actual conversation logs rather than from the number of test cases.
* Average response time, conversation turns and user satisfaction require latency logs, transcript analytics and CSAT data.
