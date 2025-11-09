# Interactive Elements - Agent 3 (Interactive Developer)

**Agent**: Agent 3 - Interactive Developer
**Status**: ⏳ Awaiting Deployment
**Dependencies**:
- ✅ Research files complete (research/)
- ⏳ shared-data.json created by Research Agent
- ⏳ Content files created by Agent 1 (READ ONLY)
**Execution Mode**: Parallel with Agent 2 (MUST wait for shared-data.json)

---

## 🎯 Agent 3 Mission

Create **5+ interactive elements** including QR codes, web portal, and optional demos. All interactive elements must use data from the **Knowledge Graph API** and design system compliance.

**Quality Target**: 9.5/10 professional interactive design
**Data Source**: **MANDATORY Knowledge Graph API**
- **API URL**: `https://kg-student-backend.ambitiouswave-220155c4.eastus2.azurecontainerapps.io`
- **Frontend**: `https://purple-ocean-0a69d8a0f.3.azurestaticapps.net`
**Total Deliverables**: 5+ interactive files

---

## ⚠️ CRITICAL: Knowledge Graph API Integration

### MANDATORY Data Source

**ALL team data MUST come from the Knowledge Graph API**. NO other sources are acceptable.

```python
# MANDATORY: Query Knowledge Graph API
import requests

KG_API_URL = "https://kg-student-backend.ambitiouswave-220155c4.eastus2.azurecontainerapps.io"

def fetch_team_data_from_kg_api():
    """
    Query Knowledge Graph API for team data
    This is the ONLY acceptable source for team information
    """
    try:
        response = requests.get(f"{KG_API_URL}/api/graph", timeout=10)
        response.raise_for_status()
        kg_data = response.json()

        # Validate response
        assert 'team' in kg_data, "Missing 'team' key in KG response"
        assert 'members' in kg_data['team'], "Missing 'members' in KG response"

        return kg_data
    except Exception as e:
        # Fallback to cache ONLY if API fails
        print(f"⚠️ KG API failed: {e}. Using cache as fallback.")
        with open("../research/kg-data-cache.json") as f:
            return json.load(f)

# VALIDATION: Cross-check against shared-data.json
def validate_team_data_against_kg(shared_data, kg_data):
    """
    Ensure shared-data.json team info matches KG API exactly
    """
    kg_members = {m['id']: m for m in kg_data['team']['members']}

    for member_id, member_info in shared_data['team'].items():
        kg_member = kg_members.get(member_id)
        if not kg_member:
            raise ValueError(f"Member {member_id} not found in KG API")

        # Validate name matches EXACTLY
        if member_info['name'] != kg_member['name']:
            raise ValueError(
                f"Name mismatch for {member_id}: "
                f"shared-data has '{member_info['name']}', "
                f"KG has '{kg_member['name']}'"
            )

        print(f"✅ {member_info['name']} validated against KG API")
```

### Required Team Member Data (from KG API)

**EXACT Names** (from Knowledge Graph - DO NOT modify):
1. Rahil M. Harihar
2. Siddarth Bhave
3. Mathew Jerry Meleth
4. Shreyas B Subramanya

**For Each Member** (ALL from KG API):
- Name (exact spelling, capitals, middle initials)
- Title
- Email (@uw.edu)
- Core skills (list from KG)
- Key achievements (with quantified metrics from KG)
- Years of experience
- Past companies
- Education (degree, GPA)
- Match score (from team-matching.md, which uses KG data)

---

## 📁 Folder Structure

```
interactive/
├── qr-codes/          # QR code PNGs (4 files)
├── web-portal/        # HTML web page (1 file)
└── demos/             # Optional videos/GIFs (0-3 files)
```

---

## 📋 Required Deliverables (5+ Files)

### QR CODES (4 PNG files)

All QR codes: **570×570 pixels**, high contrast, tested and functional

#### 1. Team Portal QR Code
**File**: `sap-team-portal-qr-v1.png`

**Destination URL**: `https://purple-ocean-0a69d8a0f.3.azurestaticapps.net`
**Purpose**: Link to Knowledge Graph frontend showing team profiles

**QR Code Generation**:
```python
import qrcode

def generate_qr_code(url, filename, size=570):
    """
    Generate high-quality QR code
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#1E3A8A", back_color="#F8FAFC")  # Navy on off-white
    img = img.resize((size, size))
    img.save(filename)
    print(f"✅ QR code saved: {filename}")

# Generate
generate_qr_code(
    "https://purple-ocean-0a69d8a0f.3.azurestaticapps.net",
    "qr-codes/sap-team-portal-qr-v1.png"
)
```

**Testing**: Verify QR code scans correctly on mobile devices

---

#### 2. Timeline QR Code
**File**: `sap-timeline-qr-v1.png`

**Destination URL**: Link to timeline visualization (GitHub Projects or web timeline)
**Purpose**: Quick access to project timeline and milestones

**Options for Destination**:
- GitHub Projects URL (if public)
- Google Sheets timeline view
- Custom timeline HTML page

---

#### 3. Proposal QR Code
**File**: `sap-proposal-qr-v1.png`

**Destination URL**: Link to web portal or PDF download
**Purpose**: Easy access to full proposal for stakeholders

**Destination**: Self-hosted web portal (see below)

---

#### 4. GitHub Repository QR Code
**File**: `sap-github-qr-v1.png`

**Destination URL**: GitHub repository with benchmarking code
**Purpose**: Access to open-source benchmarking codebase

**Destination**: `https://github.com/[username]/sap-rpt1-benchmarking` (when created)

---

### WEB PORTAL (1 HTML file)

#### 5. SAP RPT-1 Project Web Portal
**File**: `sap-web-portal-page-v1.html`

**Purpose**: Interactive web page showcasing team, project, and methodology

**Required Sections**:

##### Section 1: Hero Banner
- Project title: "SAP RPT-1 Benchmarking Study"
- Subtitle: "University of Washington MSIM Capstone Project"
- Team logo or UW branding
- Navy Blue background with white text

##### Section 2: Team Cards (DATA FROM KNOWLEDGE GRAPH API)

**CRITICAL**: Query KG API for ALL team data

```html
<!-- Team Card Template -->
<div class="team-member-card" data-member-id="member_1">
    <div class="card-header" style="background: #1E3A8A; color: #F8FAFC;">
        <h3 id="member-1-name"><!-- FROM KG API: Rahil M. Harihar --></h3>
        <p class="title" id="member-1-title"><!-- FROM KG API: Title --></p>
    </div>
    <div class="card-body">
        <div class="match-score">
            <span class="score-label">Match Score:</span>
            <span class="score-value" style="color: #14B8A6;">
                <!-- FROM team-matching.md: 94% -->
            </span>
        </div>
        <div class="role">
            <strong>Project Role:</strong>
            <span id="member-1-role"><!-- FROM shared-data.json --></span>
        </div>
        <div class="expertise">
            <strong>Expertise:</strong>
            <ul id="member-1-skills">
                <!-- FROM KG API: core_skills array -->
                <li><!-- Skill 1 from KG --></li>
                <li><!-- Skill 2 from KG --></li>
                <li><!-- Skill 3 from KG --></li>
            </ul>
        </div>
        <div class="achievements">
            <strong>Key Achievements:</strong>
            <ul id="member-1-achievements">
                <!-- FROM KG API: key_achievements array -->
                <li><!-- Achievement 1 with quantified metric --></li>
                <li><!-- Achievement 2 with quantified metric --></li>
            </ul>
        </div>
        <div class="background">
            <p>
                <strong>Experience:</strong>
                <span id="member-1-experience"><!-- FROM KG API --></span> years
            </p>
            <p>
                <strong>Past Companies:</strong>
                <span id="member-1-companies"><!-- FROM KG API: past_companies --></span>
            </p>
            <p>
                <strong>Education:</strong>
                <span id="member-1-education"><!-- FROM KG API --></span>
            </p>
        </div>
    </div>
</div>
```

**JavaScript for Data Population**:
```javascript
// Fetch from Knowledge Graph API
async function loadTeamData() {
    const KG_API_URL = "https://kg-student-backend.ambitiouswave-220155c4.eastus2.azurecontainerapps.io";

    try {
        const response = await fetch(`${KG_API_URL}/api/graph`);
        const data = await response.json();

        // Populate each team member card
        data.team.members.forEach(member => {
            document.getElementById(`member-${member.id}-name`).textContent = member.name;
            document.getElementById(`member-${member.id}-title`).textContent = member.title;

            // Populate skills
            const skillsList = document.getElementById(`member-${member.id}-skills`);
            member.core_skills.slice(0, 3).forEach(skill => {
                const li = document.createElement('li');
                li.textContent = skill;
                skillsList.appendChild(li);
            });

            // Populate achievements
            const achievementsList = document.getElementById(`member-${member.id}-achievements`);
            member.key_achievements.slice(0, 2).forEach(achievement => {
                const li = document.createElement('li');
                li.textContent = achievement;
                achievementsList.appendChild(li);
            });

            // Populate background
            document.getElementById(`member-${member.id}-experience`).textContent = member.years_of_experience;
            document.getElementById(`member-${member.id}-companies`).textContent = member.past_companies.join(", ");
            document.getElementById(`member-${member.id}-education`).textContent = member.education;
        });

        console.log("✅ Team data loaded from Knowledge Graph API");
    } catch (error) {
        console.error("❌ Failed to load from KG API:", error);
        // Fallback to shared-data.json if API fails
        loadTeamDataFromSharedData();
    }
}

// Call on page load
document.addEventListener('DOMContentLoaded', loadTeamData);
```

##### Section 3: Project Overview
- Problem statement (1 paragraph)
- Solution approach (Three Pillars visual)
- Expected outcomes

##### Section 4: Interactive Timeline
- Embedded Gantt chart or timeline visualization
- 12-week project phases
- Milestones highlighted

##### Section 5: Methodology Overview
- Three Pillars: Models, Datasets, Evaluation
- Visual diagrams embedded (SVGs from Agent 2)

##### Section 6: Contact & Links
- Email contacts for each team member (from KG API)
- Links to GitHub repository
- QR codes for mobile access
- Link to Knowledge Graph frontend

**Design Requirements**:
- Responsive design (mobile, tablet, desktop)
- Navy Blue (#1E3A8A) primary color
- Slate Gray (#64748B) text
- Teal (#14B8A6) accents and CTAs
- Helvetica Neue font family
- 40-50% white space
- Fast load time (<2s)
- Cross-browser compatible (Chrome, Firefox, Safari, Edge)

**CSS Framework**: Use TailwindCSS or custom CSS with design system

---

### OPTIONAL DEMOS (0-3 files)

#### 6. SAP RPT-1 Inference Demo (Optional)
**File**: `sap-rpt1-demo-v1.mp4` or `.gif`

**Content**:
- Screen recording of SAP RPT-1 making predictions
- Jupyter notebook walkthrough
- 30-60 seconds, high quality

**Tools**: OBS Studio, ScreenToGif, QuickTime

---

#### 7. Results Dashboard Preview (Optional)
**File**: `sap-results-dashboard-preview-v1.gif`

**Content**:
- Animated preview of results dashboard
- Interactive charts and tables
- 10-20 seconds loop

---

#### 8. Project Walkthrough Video (Optional)
**File**: `sap-project-walkthrough-v1.mp4`

**Content**:
- 2-5 minute video explaining project
- Voiceover + screen recording
- Professional quality

---

## 🔄 Wait Protocol (MANDATORY)

Agent 3 MUST wait for shared-data.json before starting:

```python
import os, time, json

def wait_for_shared_data(timeout=300):
    start_time = time.time()
    shared_data_path = "/Users/rahilharihar/TBD-Sponsers/SAP/shared-data.json"

    while not os.path.exists(shared_data_path):
        if time.time() - start_time > timeout:
            raise TimeoutError("shared-data.json not found after 5 minutes")
        print("Waiting for shared-data.json...")
        time.sleep(5)

    with open(shared_data_path) as f:
        data = json.load(f)

    required_keys = ["team", "project"]
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing key in shared-data.json: {key}")

    print("✅ shared-data.json validated. Proceeding...")
    return data
```

---

## 📦 Output Checklist

### QR Codes (4 files)
- [ ] sap-team-portal-qr-v1.png (570×570, links to KG frontend)
- [ ] sap-timeline-qr-v1.png (570×570, links to timeline)
- [ ] sap-proposal-qr-v1.png (570×570, links to web portal)
- [ ] sap-github-qr-v1.png (570×570, links to GitHub repo)

### Web Portal (1 file)
- [ ] sap-web-portal-page-v1.html
- [ ] Responsive design (mobile, tablet, desktop)
- [ ] Team data from Knowledge Graph API
- [ ] Design system compliance
- [ ] Fast load time (<2s)
- [ ] Cross-browser tested

### Optional Demos (0-3 files)
- [ ] sap-rpt1-demo-v1.mp4 or .gif (if created)
- [ ] sap-results-dashboard-preview-v1.gif (if created)
- [ ] sap-project-walkthrough-v1.mp4 (if created)

### Knowledge Graph API Validation
- [ ] **CRITICAL**: All team data queried from KG API
- [ ] Team names match KG exactly
- [ ] Skills from KG API
- [ ] Achievements from KG API (with quantified metrics)
- [ ] Experience and past companies from KG API
- [ ] Education from KG API
- [ ] NO fabricated or hallucinated data
- [ ] Fallback to cache only if API fails

### QR Code Testing
- [ ] All QR codes scan correctly on iOS
- [ ] All QR codes scan correctly on Android
- [ ] Destination URLs correct and accessible
- [ ] High contrast for readability

### Web Portal Validation
- [ ] Design system colors exact
- [ ] JavaScript loads team data from KG API
- [ ] All team member cards populated
- [ ] Match scores displayed correctly
- [ ] Links functional
- [ ] No console errors

---

## 🚨 Critical Success Factors

### Must-Do
- ✅ Wait for shared-data.json before starting
- ✅ **Query Knowledge Graph API for ALL team data**
- ✅ Validate team names match KG exactly
- ✅ Test all QR codes on mobile devices
- ✅ Ensure web portal loads team data dynamically from KG API
- ✅ Apply design system (Navy, Slate, Teal)
- ✅ Responsive web design
- ✅ Cross-browser testing

### Must-NOT-Do
- ❌ Start before shared-data.json exists
- ❌ **Use any team data NOT from Knowledge Graph API**
- ❌ Hardcode team information (must query KG API dynamically)
- ❌ Misspell team member names
- ❌ Use untested QR codes
- ❌ Violate design system
- ❌ Create slow-loading web portal (>2s)
- ❌ Skip mobile responsiveness

---

## 📊 Quality Standards

**Interactive Quality**: 9.5/10 (professional-grade)
**Data Accuracy**: 100% (all from Knowledge Graph API)
**QR Code Functionality**: 100% (tested on iOS and Android)
**Web Portal Performance**: <2s load time
**Design Compliance**: 100% (exact hex codes, fonts)
**Total Deliverables**: 5+ files (4 QR codes + 1 HTML + optional demos)
**Timeline**: Complete in 1 day (parallel with Agent 2)

---

## ⚠️ KNOWLEDGE GRAPH API EMPHASIS

**This cannot be overstated**: ALL team data must come from the Knowledge Graph API hosted at:

**`https://kg-student-backend.ambitiouswave-220155c4.eastus2.azurecontainerapps.io`**

**Frontend**: `https://purple-ocean-0a69d8a0f.3.azurestaticapps.net`

**Validation Script** (run before delivery):
```python
def validate_against_kg_api():
    """
    Validate all team data in web portal against KG API
    """
    import requests
    from bs4 import BeautifulSoup

    # Fetch from KG API
    kg_data = requests.get(
        "https://kg-student-backend.ambitiouswave-220155c4.eastus2.azurecontainerapps.io/api/graph"
    ).json()

    # Parse HTML
    with open("web-portal/sap-web-portal-page-v1.html") as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Validate each team member
    for member in kg_data['team']['members']:
        member_id = member['id']

        # Check name
        html_name = soup.find(id=f"member-{member_id}-name").text
        kg_name = member['name']
        assert html_name == kg_name, f"Name mismatch: {html_name} != {kg_name}"

        print(f"✅ {kg_name} validated against KG API")

    print("✅✅✅ ALL team data validated against Knowledge Graph API")
```

---

**Status**: ⏳ Awaiting shared-data.json
**Owner**: Agent 3 (Interactive Developer)
**Parallel With**: Agent 2 (Visual Designer)
**Next Step**: Research Agent creates shared-data.json → Agent 3 deploys
**CRITICAL REQUIREMENT**: All team data from Knowledge Graph API - NO EXCEPTIONS
