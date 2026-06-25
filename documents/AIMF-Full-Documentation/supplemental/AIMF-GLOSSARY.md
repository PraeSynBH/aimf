# AI Management Framework (AIMF) by PraeSyn
## Glossary

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0
**Publication Date**: January 29, 2026
**Status**: Pre-Publication (Working Draft)
**Document Type**: Reference

---

## Overview

This glossary defines key terms and concepts used throughout the AI Management Framework (AIMF). Terms are organized alphabetically and include references to relevant standards where applicable.

---

## A

**AI Actor**
> Any individual, group, or organization involved in the AI system lifecycle. Includes developers, deployers, operators, evaluators, end users, and impacted individuals or communities.
>
> *Source: NIST AI RMF 1.0*

**AI Incident**
> An event where an AI system causes or contributes to harm, including safety, security, privacy, fairness, or ethical violations. Includes near-misses that did not result in actual harm but could have.
>
> *AIMF Definition*

**AI Lifecycle**
> All phases of AI system development, deployment, and operation, including: planning, design, data collection, model development, validation, deployment, monitoring, maintenance, and decommissioning.
>
> *Source: ISO 42001:2023*

**AI Management System (AIMS)**
> A management system for directing and controlling an organization with regard to AI, including policies, processes, procedures, and resources.
>
> *Source: ISO 42001:2023*

**AI System**
> A machine-based system that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments.
>
> *Source: ISO/IEC 22989 (AI Concepts and Terminology)*

**Algorithmic Bias**
> Systematic and repeatable errors in AI system outputs that create unfair outcomes, often caused by biased training data, model design choices, or feedback loops.
>
> *AIMF Definition*

---

## B

**Baseline (B1/B2/B3)**
> Risk-based control scoping mechanism that determines which controls apply based on AI system characteristics. Organizations assess AI systems using a risk characterization questionnaire to determine the appropriate baseline:
> - **B1 (Low Risk)**: 23 foundational controls (~32% of framework) for low-impact AI systems
> - **B2 (Moderate Risk)**: 61 comprehensive controls (~85% of framework) for customer-facing, business-critical AI
> - **B3 (High Risk)**: All 72 controls (100% of framework) for autonomous, life-safety, or highly regulated AI
>
> *AIMF Definition*

**Baseline-Relative Score**
> An organization's actual maturity score expressed as a percentage of the maximum possible score for their applicable baseline. Formula: (Actual Score / Baseline Max Score) × 100%. Shows how much of the risk-appropriate control set has been addressed.
>
> *AIMF Scoring Metric*

---

## C

**Control**
> A safeguard or countermeasure implemented to address AI risks. In AIMF, controls are organized across four functions (GOVERN, MAP, MEASURE, MANAGE) and can be implemented at different tiers (B1, B2, B3).
>
> *AIMF Definition*

**Capability Dimension**
> One of four organizational capability areas in AIMF: Governance & Accountability, Data Management & Privacy, Technical Operations & MLOps, and Organizational Culture & Capabilities. Dimensions provide a structured view of organizational AI maturity.
>
> *AIMF Definition*

---

## D

**Data Drift**
> Changes in the statistical properties of input data over time that can degrade AI system performance. Includes covariate drift (input distribution changes), prior probability drift (label distribution changes), and concept drift (relationship between inputs and outputs changes).
>
> *AIMF Definition*

**Deployer**
> An entity that uses an AI system to provide services or make decisions affecting individuals or organizations.
>
> *Source: EU AI Act*

**Developer**
> An entity that designs, codes, or produces an AI system, including through outsourcing or by incorporating components from other sources.
>
> *Source: EU AI Act*

**Differential Privacy**
> A mathematical framework for measuring and limiting privacy loss when analyzing sensitive datasets. Provides statistical guarantees that individual data points cannot be identified or re-identified from AI system outputs.
>
> *AIMF Definition*

---

## E

**Explainability**
> The extent to which internal mechanics and outputs of an AI system can be explained in human-understandable terms. Differs from interpretability (understanding model structure) and transparency (access to information).
>
> *AIMF Definition - informed by NIST AI RMF*

**Executive Order 14110**
> U.S. Executive Order on Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence (October 30, 2023). Establishes federal AI policy including safety reporting for high-risk systems, civil rights protections, and transparency requirements.
>
> *AIMF Reference*

---

## F

**Fairness**
> The absence of bias or discrimination against individuals or groups based on inherent or acquired characteristics. In AI, fairness can be measured using multiple metrics (demographic parity, equal opportunity, equalized odds, etc.), which may conflict.
>
> *AIMF Definition - informed by NIST AI RMF*

**Framework Profile**
> A pre-defined selection and prioritization of AIMF controls tailored to specific organizational contexts, risk levels, or industry requirements. Created by PraeSyn as templates (e.g., Foundational, Healthcare, Financial Services).
>
> *AIMF Definition - adapted from NIST CSF 2.0*

**Framework-Relative Score**
> An organization's actual maturity score expressed as a percentage of the absolute maximum score across all 72 framework controls. Formula: (Actual Score / 288 points) × 100%. Enables universal benchmarking regardless of baseline or profile. See also: Profile Score, Baseline-Relative Score.
>
> *AIMF Scoring Metric*

**Function**
> One of four core categories in AIMF's control structure, aligned with NIST AI RMF: GOVERN (establish AI governance), MAP (understand context and risks), MEASURE (assess and test AI systems), MANAGE (respond to and monitor risks).
>
> *AIMF Definition - based on NIST AI RMF*

---

## G

**Generative AI**
> AI systems that generate new content (text, images, code, audio, video) based on patterns learned from training data. Examples include large language models (LLMs) and text-to-image models.
>
> *AIMF Definition*

**GOVERN Function**
> The AIMF function establishing organizational structures, policies, and culture for AI risk management. Includes 19 controls covering legal compliance, accountability, risk management, organizational structure, stakeholder engagement, and capability development.
>
> *AIMF Definition*

---

## H

**High-Risk AI**
> AI systems that pose significant risk to health, safety, fundamental rights, or critical infrastructure. Regulatory frameworks (EU AI Act, Executive Order 14110) define specific high-risk categories requiring enhanced governance and oversight.
>
> *AIMF Definition - informed by EU AI Act*

**Human-in-the-Loop (HITL)**
> AI system design where human judgment and oversight are integrated into critical decision points. Humans can review, modify, or override AI recommendations before actions are taken.
>
> *AIMF Definition*

**Human-on-the-Loop (HOTL)**
> AI system design where humans monitor system operation and can intervene if necessary, but the AI operates autonomously for most decisions. Humans supervise but do not review every output.
>
> *AIMF Definition*

---

## I

**Implementation Profile**
> An organization-specific customization of a framework profile documenting actual control selections, tier assignments, implementation status, and deviations. Created by organizations using AIMF.
>
> *AIMF Definition - adapted from NIST CSF 2.0*

**Implementation Profile**
> An organization-specific customization of a framework profile documenting actual control selections, baseline assignments, target maturity levels, implementation status, and deviations. Created by organizations using AIMF to document their actual implementation decisions.
>
> *AIMF Definition - adapted from NIST CSF 2.0*

**Impact Assessment**
> Systematic evaluation of potential effects (positive and negative) of an AI system on individuals, groups, organizations, and society. Includes privacy impact assessment (PIA), data protection impact assessment (DPIA), civil rights impact assessment, and environmental impact assessment.
>
> *AIMF Definition - informed by ISO 42001*

**Inference**
> The process of using a trained AI model to generate outputs (predictions, classifications, recommendations) based on new input data. Distinct from training (building the model).
>
> *AIMF Definition*

---

## M

**MANAGE Function**
> The AIMF function for managing identified AI risks through response plans, monitoring, and continuous improvement. Includes 13 controls covering incident response, risk mitigation, third-party management, post-deployment monitoring, and value preservation.
>
> *AIMF Definition*

**MAP Function**
> The AIMF function for understanding AI system context, purposes, and associated risks. Includes 19 controls covering requirements definition, team composition, categorization, impact assessment, stakeholder engagement, and third-party risk.
>
> *AIMF Definition*

**Maturity Level (ML1-5)**
> The quality of control implementation measured on a 5-level CMMI-based scale:
> - **ML1 (Initial)**: Ad-hoc, undocumented, individual-dependent (0 points)
> - **ML2 (Developing)**: Documented but inconsistent (1 point)
> - **ML3 (Defined)**: Standardized, organization-wide (2 points) — *Default target*
> - **ML4 (Managed)**: Quantitatively measured and controlled (3 points)
> - **ML5 (Optimizing)**: Continuous improvement and innovation (4 points)
>
> Maturity levels are assessed per control and are orthogonal to baseline selection. A B1 (low-risk) control can be implemented at ML5 (optimizing), and a B3 (high-risk) control may be at ML1 (initial), revealing gaps.
>
> *AIMF Definition - based on CMMI*

**MEASURE Function**
> The AIMF function for assessing, testing, and validating AI systems against trustworthiness criteria. Includes 22 controls covering TEVV (Test, Evaluation, Validation, and Verification), testing documentation, performance metrics, fairness, safety, security, privacy, transparency, and explainability.
>
> *AIMF Definition*

**Model Card**
> Structured documentation describing an AI model's intended uses, performance characteristics, limitations, training data, ethical considerations, and evaluation results. Promotes transparency and informed use.
>
> *Source: Mitchell et al., Google Research (2019)*

**Model Drift**
> Degradation in AI model performance over time due to changes in data distributions, relationships, or operational environment. Requires monitoring and potential model retraining.
>
> *AIMF Definition*

---

## P

**Pre-trained Model**
> An AI model trained on large datasets and made available for fine-tuning or direct use by other organizations. Includes foundation models like large language models (LLMs). Requires third-party risk management.
>
> *AIMF Definition*

**Profile (Framework Profile)**
> See Framework Profile.

**Profile Attribution**
> Specification of how hierarchical profiles aggregate control assessments from child profiles to parent profiles. Three types: (1) Direct — assessed at this level, (2) Single — one child fully owns the control (100% attribution), (3) Distributed — multiple children share responsibility (equal or weighted). Profile builders must explicitly specify attribution for each control.
>
> *AIMF Definition*

**Profile Score**
> An organization's actual maturity score expressed as a percentage of their profile's target score. Formula: (Actual Score / Profile Target Score) × 100%. Measures whether the organization is meeting its profiled obligations. Default target is ML3 (2 points) per control.
>
> *AIMF Scoring Metric*

**Profile Target Maturity**
> The expected maturity level for each control in a profile. Default is ML3 (Defined - standardized, organization-wide). Profiles can customize per control (e.g., ML4 for critical safety controls, ML2 for lower-priority controls). Enables maturity expectations to increase over time without changing control scope.
>
> *AIMF Definition*

**Protected Health Information (PHI)**
> Individually identifiable health information created, received, or maintained by covered entities under HIPAA. AI systems processing PHI require privacy and security safeguards.
>
> *Source: HIPAA Privacy Rule*

---

## R

**Red Teaming**
> Security testing where adversaries attempt to find vulnerabilities, bypass safeguards, or cause harmful outputs in AI systems. Common for generative AI to identify risks like prompt injection, jailbreaks, or harmful content generation.
>
> *AIMF Definition*

**Residual Risk**
> Risk remaining after controls have been implemented. Organizations must explicitly accept residual risks through documented risk acceptance decisions.
>
> *AIMF Definition - informed by ISO 31000*

---

## S

**Software as a Medical Device (SaMD)**
> Software intended to be used for medical purposes (diagnosis, treatment, monitoring) without being part of a hardware medical device. AI-based diagnostic or clinical decision support systems may qualify as SaMD requiring FDA regulation.
>
> *Source: FDA*

**Stakeholder**
> Any individual, group, or organization with interest in or affected by an AI system. Includes developers, deployers, users, impacted individuals, regulators, civil society, and communities.
>
> *Source: NIST AI RMF 1.0*

---

## T

**TEVV (Test, Evaluation, Validation, and Verification)**
> Systematic processes for assessing AI system quality, trustworthiness, and performance: Testing (checking functionality), Evaluation (measuring against criteria), Validation (confirming it solves the right problem), Verification (ensuring it meets specifications).
>
> *Source: NIST AI RMF 1.0*

**Third-Party AI**
> AI systems, models, or components developed by external vendors or open-source communities and integrated into an organization's systems. Requires vendor risk management, contractual safeguards, and ongoing monitoring.
>
> *AIMF Definition*

**Tier**
> See **Implementation Tier**

**Transparency**
> The extent to which information about an AI system is available and accessible to stakeholders. Includes documentation, disclosures about capabilities and limitations, and communication about AI system use.
>
> *AIMF Definition - informed by NIST AI RMF*

**Trustworthy AI**
> AI systems that are valid, reliable, safe, secure, resilient, accountable, explainable, interpretable, privacy-enhanced, and fair. Trustworthiness is assessed across multiple dimensions, not a binary state.
>
> *Source: NIST AI RMF 1.0*

---

## V

**Validation**
> Confirmation that an AI system fulfills its intended use and requirements in its operational environment. Answers "are we building the right system?"
>
> *AIMF Definition - informed by ISO 42001*

**Verification**
> Confirmation that an AI system meets specified requirements and design specifications. Answers "are we building the system right?"
>
> *AIMF Definition - informed by ISO 42001*

---

## References

- **ISO/IEC 22989:2022**: Information technology — Artificial intelligence — Concepts and terminology
- **ISO/IEC 42001:2023**: Information technology — Artificial intelligence — Management system
- **NIST AI Risk Management Framework (AI RMF) 1.0** (January 2023)
- **EU Artificial Intelligence Act** (Regulation (EU) 2024/1689)
- **Executive Order 14110**: Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence (October 2023)
- **CMMI (Capability Maturity Model Integration)**: Maturity level framework from Software Engineering Institute

---

**AI Management Framework (AIMF) by PraeSyn**

*This glossary will be updated in future AIMF versions as terminology evolves and new standards emerge.*
