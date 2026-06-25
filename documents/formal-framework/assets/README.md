# AI Management Framework (AIMF) by PraeSyn
## Assets Directory

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0
**Publication Date**: January 25, 2026

---

## Overview

This directory contains visual assets and templates for the AI Management Framework (AIMF). Assets include diagram specifications, templates for implementation, and supporting materials for presentations and documentation.

---

## Directory Structure

```
assets/
├── README.md (this file)
├── diagrams/               # Visual diagram specifications
│   ├── framework-architecture-diagram.md
│   ├── maturity-progression-diagram.md
│   ├── tier-comparison-infographic.md
│   ├── profile-selection-flowchart.md
│   └── standards-integration-diagram.md
└── templates/              # Implementation templates
    ├── profile-customization-template.md
    └── assessment-workbook-template.md
```

---

## Diagrams

### 1. Framework Architecture Diagram
**File**: `diagrams/framework-architecture-diagram.md`

**Purpose**: Illustrates the complete AIMF architecture showing relationships between maturity levels, dimensions, tiers, functions, and profiles.

**Use Cases**:
- Executive presentations introducing AIMF
- Framework overview for training materials
- Website and marketing collateral
- Conference presentations

**Format**: Layered architecture with standards foundation, control framework, dimensions, maturity levels, tiers, and profiles

**Rendering Guidance**:
- Includes Mermaid diagram code for interactive rendering
- Text-based ASCII art for quick reference
- Detailed specifications for professional graphic design

---

### 2. Maturity Progression Diagram
**File**: `diagrams/maturity-progression-diagram.md`

**Purpose**: Shows the 5 maturity levels with characteristics, progression paths, and typical timelines.

**Use Cases**:
- Maturity assessment presentations
- Implementation planning
- Showing progression roadmap to stakeholders
- Benchmarking organizational position

**Format**: Horizontal progression or staircase showing advancement from Level 1 to Level 5

**Rendering Guidance**:
- Color-coded by maturity level (gray → gray-blue → blue → teal → green)
- Includes transition timelines and resource requirements
- Radar chart option for dimensional assessment

---

### 3. Tier Comparison Infographic
**File**: `diagrams/tier-comparison-infographic.md`

**Purpose**: Compares the three implementation tiers (T1, T2, T3) showing requirements, scope, and use cases.

**Use Cases**:
- Tier selection decision support
- Budget planning (show resource differences)
- Risk assessment presentations
- Implementation scoping

**Format**: Three-column comparison table with consistent structure across criteria

**Rendering Guidance**:
- Color scheme: Gray (T1), Blue (T2), Orange (T3)
- Includes decision flowchart for "which tier?"
- Tabular format for easy comparison

---

### 4. Profile Selection Flowchart
**File**: `diagrams/profile-selection-flowchart.md`

**Purpose**: Guides organizations through systematic profile selection based on industry, risk, and organizational characteristics.

**Use Cases**:
- Initial AIMF engagement (which profile to start with?)
- Profile assessment for existing implementations
- Stakeholder communication about profile rationale
- Profile customization planning

**Format**: Decision tree flowchart with multiple endpoints for each profile

**Rendering Guidance**:
- Interactive decision tree (web) or static flowchart (print)
- Includes self-assessment checklist
- Profile decision matrix for quick reference

---

### 5. Standards Integration Diagram
**File**: `diagrams/standards-integration-diagram.md`

**Purpose**: Illustrates how AIMF integrates with international standards, regulatory frameworks, and industry guidelines.

**Use Cases**:
- Demonstrating standards compliance
- Certification preparation (ISO 42001)
- Regulatory audit support
- Marketing AIMF's comprehensive approach

**Format**: Hub-and-spoke or layered integration showing AIMF connections to external standards

**Rendering Guidance**:
- Central AIMF hub with connections to standards
- Line thickness indicates strength of integration
- Includes coverage summary table

---

## How to Use These Specifications

### For Graphic Designers

Each diagram specification includes:
1. **Visual Description**: Detailed layout and structure guidance
2. **Color Palette**: Specific hex codes for brand consistency
3. **Content Elements**: All text, labels, and data points
4. **Visual Treatment**: Style guidance for icons, lines, and shapes
5. **Usage Guidelines**: Context for where/how diagram is used

**Recommended Tools**:
- Adobe Illustrator for professional vector graphics
- Figma for collaborative design
- PowerPoint/Keynote for presentation versions
- Mermaid Live Editor for interactive diagrams

### For Developers

**Mermaid Diagrams**:
- All specifications include Mermaid diagram code
- Render using Mermaid.js in web applications
- Markdown-compatible for documentation

**Example Integration**:
```javascript
import mermaid from 'mermaid';
mermaid.initialize({ startOnLoad: true });
```

### For Content Creators

**Quick Reference**:
- Text-based ASCII art for quick understanding
- Tables for presentations and reports
- Mermaid code for interactive documentation

**Presentation Tips**:
- Use simplified versions for executive audiences
- Build animations for training (reveal layers progressively)
- Combine multiple diagrams for comprehensive overview

---

## Templates

### 1. Profile Customization Template
**File**: `templates/profile-customization-template.md` (coming soon)

**Purpose**: Template for organizations to document their custom implementation profile.

**Contents**:
- Organization information and context
- Profile foundation (which framework profile selected)
- Control customizations (additions/removals)
- Tier assignments by AI system
- Implementation timeline and phases
- Success criteria and metrics

**Use Cases**:
- Creating organization-specific implementation profiles
- Documenting profile deviations with rationale
- Tracking implementation progress

---

### 2. Assessment Workbook Template
**File**: `templates/assessment-workbook-template.md` (coming soon)

**Purpose**: Template for conducting AIMF maturity assessments.

**Contents**:
- Assessment scope and methodology
- Control-by-control assessment questions
- Scoring rubric (0-3 scale)
- Evidence requirements
- Maturity level calculation
- Gap analysis and recommendations

**Use Cases**:
- Self-assessments
- External audits
- Baseline establishment
- Progress tracking

---

## Rendering Recommendations

### For Print Materials
- **Resolution**: Minimum 300 DPI for diagrams
- **Format**: PDF or high-resolution PNG
- **Color**: CMYK color space for professional printing
- **Fonts**: Embed fonts to ensure consistency

### For Digital Materials
- **Resolution**: 1920x1080 or larger for presentations
- **Format**: SVG for scalability, PNG for compatibility
- **Color**: RGB color space
- **Interactive**: Consider Mermaid for web documentation

### For Presentations
- **Slide Size**: 16:9 aspect ratio (standard)
- **Animation**: Build diagrams layer-by-layer for complex visuals
- **Clarity**: Ensure text readable at projected size (minimum 18pt)
- **Consistency**: Use same color palette across all slides

---

## Brand Guidelines

### Color Palette

**Primary Colors**:
- Blue: #1E3A8A (governance, structure, trust)
- Teal: #0D9488 (progression, growth, maturity)
- Orange: #EA580C (high-risk, attention, critical)
- Gray: #64748B (foundational, neutral, supporting)

**Accent Colors**:
- Light Blue: #3B82F6
- Green: #059669 (success, optimization)
- Purple: #7C3AED (measurement, analysis)

**Neutral Colors**:
- White: #FFFFFF
- Light Gray: #F8FAFC
- Dark Gray: #1E293B

### Typography

**Recommended Fonts**:
- **Headings**: Inter, Helvetica Neue, or Arial (bold)
- **Body Text**: Inter, Helvetica, or Arial (regular)
- **Code/Technical**: Fira Code, Consolas, or Monaco

**Font Sizes** (presentations):
- Title: 36-48pt
- Headings: 24-32pt
- Body: 18-24pt
- Captions: 14-16pt

---

## License and Usage

**License**: CC BY-NC-ND 4.0

**Permitted Uses**:
- Educational and non-commercial use
- Implementation within your organization
- Presentations and training materials
- Consulting engagements using AIMF

**Attribution Required**:
> "AI Management Framework (AIMF) by PraeSyn, LLC. Licensed under CC BY-NC-ND 4.0."

**Restrictions**:
- No modifications to diagram specifications (use as-is or customize for your implementation)
- No commercial redistribution of AIMF assets
- No removal of attribution

---

## Contributing

### Suggesting Improvements

To suggest improvements to visual assets:
1. Identify the specific diagram and issue
2. Provide clear description of suggested change
3. Explain rationale (clarity, accuracy, usability)
4. Submit via [feedback channel TBD]

### Sharing Custom Visuals

If you create professional renderings of these diagrams:
- Consider sharing back to the community (optional)
- Ensure attribution to AIMF by PraeSyn
- Follow brand guidelines

---

## Future Enhancements

**Planned Additions** (v1.1+):
- Interactive web-based diagram explorer
- Animated versions for training videos
- Printable quick reference cards
- PowerPoint/Keynote template deck
- Figma design system

**Community Requests**:
- Additional language translations
- Industry-specific diagram variations
- Simplified versions for non-technical audiences

---

## Contact and Support

For questions about visual assets or to request custom renderings:
- Email: [contact information TBD]
- Website: [URL TBD]

For professional graphic design services or custom diagrams:
- PraeSyn Consulting: [contact information TBD]

---

**AI Management Framework (AIMF) by PraeSyn**

*These visual assets are designed to communicate AIMF concepts clearly and professionally. Use them to educate stakeholders, guide implementation, and demonstrate standards alignment.*

**Last Updated**: January 25, 2026 (v1.0 release)
