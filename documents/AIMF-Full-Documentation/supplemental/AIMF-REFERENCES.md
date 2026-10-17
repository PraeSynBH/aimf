# AI Management Framework (AIMF) by PraeSyn
## References and Bibliography

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0
**Publication Date**: January 29, 2026
**Status**: Pre-Publication (Working Draft)
**Document Type**: Reference

---

## Overview

This document provides comprehensive references for all standards, regulations, research, and external frameworks referenced in the AI Management Framework (AIMF). Citations are organized by category for ease of navigation.

---

## Primary Standards and Frameworks

### ISO/IEC Standards

**ISO/IEC 42001:2023 - Information technology — Artificial intelligence — Management system**
- **Published**: December 2023
- **Publisher**: International Organization for Standardization (ISO) / International Electrotechnical Commission (IEC)
- **Scope**: Requirements for establishing, implementing, maintaining, and continually improving an AI management system (AIMS)
- **Relationship to AIMF**: Primary foundation; all AIMF controls map to ISO 42001 clauses
- **Availability**: Purchase from ISO (https://www.iso.org/standard/81230.html)

**ISO/IEC 22989:2022 - Information technology — Artificial intelligence — Concepts and terminology**
- **Published**: July 2022
- **Publisher**: ISO/IEC
- **Scope**: Defines fundamental AI concepts and terminology
- **Relationship to AIMF**: Source for AI system definitions and taxonomy
- **Availability**: Purchase from ISO (https://www.iso.org/standard/74296.html)

**ISO/IEC 23894:2023 - Information technology — Artificial intelligence — Guidance on risk management**
- **Published**: March 2023
- **Publisher**: ISO/IEC
- **Scope**: Guidance for organizations on managing AI-specific risks
- **Relationship to AIMF**: Informs AIMF risk management controls (MANAGE function)
- **Availability**: Purchase from ISO (https://www.iso.org/standard/77304.html)

**ISO/IEC 27001:2022 - Information security, cybersecurity and privacy protection — Information security management systems — Requirements**
- **Published**: October 2022
- **Publisher**: ISO/IEC
- **Scope**: Requirements for information security management systems
- **Relationship to AIMF**: AIMF security controls (MEA-2.7) map to ISO 27001 Annex A
- **Availability**: Purchase from ISO (https://www.iso.org/standard/82875.html)

---

### NIST Frameworks

**NIST AI Risk Management Framework (AI RMF) 1.0**
- **Published**: January 26, 2023
- **Publisher**: National Institute of Standards and Technology (NIST), U.S. Department of Commerce
- **Document**: NIST AI 100-1
- **Scope**: Framework for managing AI risks across the AI lifecycle
- **Relationship to AIMF**: AIMF's 4 functions (GOVERN, MAP, MEASURE, MANAGE) align with NIST AI RMF; all 72 NIST subcategories mapped to AIMF controls
- **Availability**: Free download (https://www.nist.gov/itl/ai-risk-management-framework)

**NIST Cybersecurity Framework (CSF) 2.0**
- **Published**: February 26, 2024
- **Publisher**: NIST
- **Document**: NIST CSWP 29
- **Scope**: Framework for managing cybersecurity risks
- **Relationship to AIMF**: AIMF profile methodology adapted from NIST CSF 2.0 Community Profiles approach
- **Availability**: Free download (https://www.nist.gov/cyberframework)

**NIST Special Publication 1270 - Towards a Standard for Identifying and Managing Bias in Artificial Intelligence**
- **Published**: March 2022 (Draft)
- **Publisher**: NIST
- **Document**: NIST SP 1270
- **Scope**: Guidance on identifying and managing bias in AI systems
- **Relationship to AIMF**: Informs MEA-2.11 (Fairness Assessment) control guidance
- **Availability**: Free download (https://www.nist.gov/publications/towards-standard-identifying-and-managing-bias-artificial-intelligence)

---

## U.S. Federal Regulations and Policy

### Executive Orders

**Executive Order 14110: Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence**
- **Issued**: October 30, 2023
- **President**: Joseph R. Biden Jr.
- **Key Provisions**:
  - High-risk AI safety reporting requirements
  - Civil rights protections for AI systems
  - Transparency and public accountability
  - Agency AI governance requirements
- **Relationship to AIMF**: Government Profile addresses EO 14110 requirements; complete mapping in AIMF-EXECUTIVE-ORDER-14110-MAPPING.md
- **Availability**: Federal Register (https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence)

**Executive Order 14179: Advancing Artificial Intelligence Innovation**
- **Issued**: December 2024 (hypothetical - verify actual EO number and title)
- **President**: [Verify]
- **Key Provisions**: Federal AI innovation, research investment, international collaboration
- **Relationship to AIMF**: Supplementary to EO 14110; mapping in AIMF-EXECUTIVE-ORDER-14179-MAPPING.md
- **Availability**: Federal Register [URL TBD]

### OMB Guidance

**OMB Memorandum M-24-10: Advancing Governance, Innovation, and Risk Management for Agency Use of Artificial Intelligence**
- **Issued**: March 28, 2024
- **Agency**: Office of Management and Budget (OMB)
- **Key Provisions**: Federal agency AI governance requirements, minimum practices, impact assessments
- **Relationship to AIMF**: Government Profile aligns with OMB AI governance expectations
- **Availability**: WhiteHouse.gov (https://www.whitehouse.gov/omb/briefing-room/2024/03/28/m-24-10-memorandum-for-the-heads-of-executive-departments-and-agencies/)

---

## European Union Regulations

**Regulation (EU) 2024/1689: Artificial Intelligence Act (EU AI Act)**
- **Adopted**: May 21, 2024
- **Effective**: August 1, 2024 (phased implementation through 2026-2027)
- **Authority**: European Parliament and Council of the European Union
- **Scope**: Harmonized rules on AI across EU member states; risk-based approach (unacceptable, high-risk, limited risk, minimal risk)
- **Key Requirements**: Conformity assessments, transparency obligations, fundamental rights protections, high-risk AI systems requirements
- **Relationship to AIMF**: High-Assurance Profile supports high-risk AI requirements under EU AI Act (conformity assessment, documentation, human oversight)
- **Availability**: EUR-Lex (https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

**General Data Protection Regulation (GDPR) - Regulation (EU) 2016/679**
- **Effective**: May 25, 2018
- **Authority**: European Parliament and Council
- **Scope**: Data protection and privacy for EU citizens
- **Relationship to AIMF**: MEA-2.10 (Privacy Evaluation) addresses GDPR requirements for AI systems processing personal data
- **Availability**: EUR-Lex (https://eur-lex.europa.eu/eli/reg/2016/679/oj)

---

## U.S. Healthcare Regulations

**Health Insurance Portability and Accountability Act (HIPAA)**
- **Privacy Rule**: 45 CFR Part 160 and Part 164, Subparts A and E
- **Security Rule**: 45 CFR Part 164, Subparts A and C
- **Authority**: U.S. Department of Health and Human Services (HHS)
- **Scope**: Protected health information (PHI) privacy and security
- **Relationship to AIMF**: Healthcare Profile addresses HIPAA compliance for AI systems processing PHI
- **Availability**: HHS.gov (https://www.hhs.gov/hipaa/index.html)

**FDA Regulations: Software as a Medical Device (SaMD)**
- **Regulation**: 21 CFR Part 880 (Medical Device Data Systems)
- **Guidance**: "Clinical Decision Support Software" (September 2022)
- **Authority**: U.S. Food and Drug Administration (FDA)
- **Scope**: Medical device regulations for AI-based diagnostic and clinical decision support systems
- **Relationship to AIMF**: Healthcare Profile addresses FDA requirements including Quality Management System (QMS), validation, post-market surveillance
- **Availability**: FDA.gov (https://www.fda.gov/medical-devices/software-medical-device-samd)

**Clinical Laboratory Improvement Amendments (CLIA)**
- **Regulation**: 42 CFR Part 493
- **Authority**: Centers for Medicare & Medicaid Services (CMS)
- **Scope**: Laboratory testing quality standards
- **Relationship to AIMF**: Healthcare Profile considers CLIA when AI is used for diagnostic purposes
- **Availability**: CMS.gov (https://www.cms.gov/regulations-and-guidance/legislation/clia)

---

## U.S. Financial Services Regulations

**Gramm-Leach-Bliley Act (GLBA)**
- **Regulation**: 15 USC §6801 et seq.; implementing regulations by FTC, banking agencies
- **Authority**: Federal Trade Commission (FTC), federal banking regulators
- **Scope**: Financial institution privacy and data security
- **Relationship to AIMF**: Financial Services Profile addresses GLBA privacy requirements
- **Availability**: FTC.gov (https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act)

**Fair Credit Reporting Act (FCRA)**
- **Regulation**: 15 USC §1681 et seq.
- **Authority**: FTC, Consumer Financial Protection Bureau (CFPB)
- **Scope**: Credit reporting accuracy, fairness, privacy
- **Relationship to AIMF**: Financial Services Profile addresses FCRA requirements including adverse action explanations
- **Availability**: FTC.gov (https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act)

**Equal Credit Opportunity Act (ECOA)**
- **Regulation**: 15 USC §1691 et seq.; Regulation B (12 CFR Part 1002)
- **Authority**: CFPB
- **Scope**: Prohibition of credit discrimination; adverse action notice requirements
- **Relationship to AIMF**: Financial Services Profile fairness requirements (MEA-2.11) address ECOA compliance
- **Availability**: CFPB.gov (https://www.consumerfinance.gov/rules-policy/regulations/1002/)

**SR 11-7: Guidance on Model Risk Management**
- **Issued**: April 4, 2011 (updated periodically)
- **Authority**: Federal Reserve, Office of the Comptroller of the Currency (OCC)
- **Scope**: Model risk management for regulated financial institutions
- **Relationship to AIMF**: Financial Services Profile aligns with SR 11-7 expectations (independent validation, model governance, back-testing)
- **Availability**: FederalReserve.gov (https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm)

---

## State AI Laws (United States)

**Colorado Artificial Intelligence Act (SB 24-205)**
- **Enacted**: May 17, 2024
- **Effective**: February 1, 2026
- **Scope**: High-risk AI systems; deployer and developer requirements; algorithmic discrimination prevention
- **Relationship to AIMF**: Balanced and High-Assurance profiles support Colorado AI Act requirements
- **Availability**: Colorado General Assembly (https://leg.colorado.gov/bills/sb24-205)

**California AB 302: Automated Decision Tools**
- **Enacted**: 2024 (verify date)
- **Effective**: 2025 (verify date)
- **Scope**: State agency AI inventory, impact assessments, public reporting
- **Relationship to AIMF**: Government Profile addresses California state agency requirements
- **Availability**: California Legislature (https://leginfo.legislature.ca.gov/)

---

## Maturity and Capability Models

**CMMI (Capability Maturity Model Integration)**
- **Version**: CMMI V2.0
- **Published**: 2018 (updated periodically)
- **Publisher**: CMMI Institute (part of ISACA)
- **Scope**: Process improvement and capability maturity assessment
- **Relationship to AIMF**: AIMF's 5 maturity levels adapted from CMMI maturity framework
- **Availability**: ISACA.org (https://cmmiinstitute.com/)

**NIST Cybersecurity Framework Tiers**
- **Source**: NIST CSF 1.0 (2014), updated in CSF 2.0 (2024)
- **Publisher**: NIST
- **Scope**: Implementation tiers (Partial, Risk Informed, Repeatable, Adaptive)
- **Relationship to AIMF**: Informed AIMF's tier structure (B1, B2, B3)
- **Availability**: NIST CSF 2.0 documentation

---

## Research and Technical Papers

**Model Cards for Model Reporting**
- **Authors**: Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, Timnit Gebru
- **Published**: 2019, Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT* 2019)
- **Scope**: Structured documentation for AI/ML models
- **Relationship to AIMF**: MEA-2.8 (Transparency) references model cards as best practice
- **Availability**: ACM Digital Library (https://doi.org/10.1145/3287560.3287596)

**Datasheets for Datasets**
- **Authors**: Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III, Kate Crawford
- **Published**: 2018, Proceedings of the 5th Workshop on Fairness, Accountability, and Transparency in Machine Learning (FAT/ML 2018)
- **Scope**: Structured documentation for datasets
- **Relationship to AIMF**: MAP-1.6 (AI System Requirements) references datasheets for training data documentation
- **Availability**: arXiv (https://arxiv.org/abs/1803.09010)

**Fairness Definitions Explained**
- **Authors**: Sahil Verma, Julia Rubin
- **Published**: 2018, ACM/IEEE International Workshop on Software Fairness (FairWare 2018)
- **Scope**: Taxonomy of 20+ fairness definitions and their mathematical formulations
- **Relationship to AIMF**: MEA-2.11 (Fairness Assessment) guidance informed by fairness metrics taxonomy
- **Availability**: ACM Digital Library (https://doi.org/10.1145/3194770.3194776)

**AI Incident Database**
- **Organization**: Partnership on AI
- **Scope**: Comprehensive database of AI system incidents and failures
- **Relationship to AIMF**: Informs incident response (MAN-1.3) and risk management guidance
- **Availability**: https://incidentdatabase.ai/

---

## Industry Standards and Best Practices

**IEEE 7000-2021: Model Process for Addressing Ethical Concerns During System Design**
- **Published**: 2021
- **Publisher**: Institute of Electrical and Electronics Engineers (IEEE)
- **Scope**: Process for addressing ethical concerns in system design
- **Relationship to AIMF**: Informs GOVERN controls related to ethics and values alignment
- **Availability**: IEEE Xplore (https://standards.ieee.org/ieee/7000/7842/)

**Partnership on AI Guidelines**
- **Organization**: Partnership on AI
- **Published**: Ongoing
- **Scope**: Responsible AI development guidelines from industry consortium
- **Relationship to AIMF**: Best practices inform AIMF control guidance
- **Availability**: PartnershiponAI.org (https://partnershiponai.org/)

**Responsible AI Practices (Google)**
- **Organization**: Google AI
- **Published**: Ongoing updates
- **Scope**: Google's approach to responsible AI development
- **Relationship to AIMF**: Industry best practices for MEASURE and GOVERN controls
- **Availability**: Google AI (https://ai.google/responsibility/responsible-ai-practices/)

**Microsoft Responsible AI Standard (v2)**
- **Organization**: Microsoft
- **Published**: June 2022
- **Scope**: Microsoft's internal responsible AI standard
- **Relationship to AIMF**: Industry benchmark for comprehensive AI governance
- **Availability**: Microsoft (https://blogs.microsoft.com/on-the-issues/2022/06/21/microsofts-framework-for-building-ai-systems-responsibly/)

---

## NIST CSF Community Profiles (Reference for Future AIMF Profiles)

**NIST Internal Report (IR) 8576: Transit Cybersecurity Framework Community Profile**
- **Published**: March 2024
- **Publisher**: NIST
- **Scope**: Cybersecurity framework profile for public transportation sector
- **Relationship to AIMF**: Reference model for AIMF future sector-specific profiles
- **Availability**: NIST (https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8576.ipd.pdf)

**Preliminary Draft: Cybersecurity Framework Profile for Artificial Intelligence**
- **Published**: December 2025 (Draft for public comment)
- **Publisher**: NIST
- **Scope**: CSF profile specifically for AI cybersecurity risks
- **Relationship to AIMF**: Complementary framework focusing on AI cybersecurity; potential alignment in future AIMF versions
- **Availability**: NIST (check NIST.gov for current draft status)

---

## Additional References

**The Ethics of AI Ethics: An Evaluation of Guidelines**
- **Authors**: Thilo Hagendorff
- **Published**: 2020, Minds and Machines
- **Scope**: Analysis of AI ethics guidelines from various organizations
- **Relationship to AIMF**: Informs ethical considerations in GOVERN function
- **Availability**: Springer (https://doi.org/10.1007/s11023-020-09517-8)

**OECD AI Principles**
- **Organization**: Organisation for Economic Co-operation and Development (OECD)
- **Published**: May 2019
- **Scope**: International AI principles for responsible stewardship
- **Relationship to AIMF**: High-level principles aligned with AIMF governance objectives
- **Availability**: OECD.AI (https://oecd.ai/en/ai-principles)

**AI Risk Management Playbook**
- **Organization**: World Economic Forum (WEF)
- **Published**: January 2024
- **Scope**: Practical guidance for AI risk management
- **Relationship to AIMF**: Complementary resource for AIMF implementation
- **Availability**: WEForum.org (https://www.weforum.org/publications/advancing-responsible-ai-innovation-a-playbook/)

---

## How to Cite AIMF

**Academic Citation** (APA Style):
> PraeSyn, LLC. (2026). *AI Management Framework (AIMF) Version 1.0*. https://[URL TBD]

**Professional Reference**:
> AI Management Framework (AIMF) by PraeSyn, Version 1.0 (2026). Available under CC BY-NC-ND 4.0 license.

**In-Text Reference**:
> "According to the AI Management Framework (AIMF) by PraeSyn (2026), organizations should..."

---

## Document Updates

This references document will be updated with new standards, regulations, and research as AIMF evolves. Suggest additions by contacting PraeSyn [contact information TBD].

**Last Updated**: January 25, 2026 (v1.0 release)

---

**AI Management Framework (AIMF) by PraeSyn**

*This references document provides comprehensive citations for AIMF's foundational standards and supporting research. All external references remain the property of their respective publishers and are subject to their licensing terms.*
