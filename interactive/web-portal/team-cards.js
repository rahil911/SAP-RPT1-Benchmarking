/**
 * SAP RPT-1 Benchmarking Project - Team Cards Dynamic Loader
 *
 * CRITICAL: ALL team data MUST be loaded from Knowledge Graph API
 * NO hardcoded team data is permitted
 *
 * Knowledge Graph API: https://kg-student-backend.ambitiouswave-220155c4.eastus2.azurecontainerapps.io
 * Fallback: ../shared-data.json (only if API fails)
 */

const KG_API_BASE_URL = 'https://kg-student-backend.ambitiouswave-220155c4.eastus2.azurecontainerapps.io';

/**
 * Load team data from Knowledge Graph API
 * Primary source: KG API
 * Fallback: shared-data.json
 */
async function loadTeamData() {
    const container = document.getElementById('team-container');

    if (!container) {
        console.error('Team container not found');
        return;
    }

    // Show loading state
    container.innerHTML = '<div class="loading">Loading team data from Knowledge Graph API</div>';

    try {
        // PRIMARY: Fetch from Knowledge Graph API
        console.log('Fetching team data from Knowledge Graph API...');
        const response = await fetch(`${KG_API_BASE_URL}/api/graph`, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            mode: 'cors'
        });

        if (!response.ok) {
            throw new Error(`KG API returned ${response.status}: ${response.statusText}`);
        }

        const data = await response.json();

        // Validate response structure
        if (!data.team || !data.team.members) {
            throw new Error('Invalid KG API response structure');
        }

        console.log('✅ Team data loaded from Knowledge Graph API');
        renderTeamCards(data.team.members, 'Knowledge Graph API');

    } catch (error) {
        console.error('❌ KG API failed:', error);
        console.log('Attempting fallback to shared-data.json...');

        try {
            // FALLBACK: Load from shared-data.json
            const fallbackResponse = await fetch('../../shared-data.json');

            if (!fallbackResponse.ok) {
                throw new Error(`Fallback failed: ${fallbackResponse.status}`);
            }

            const fallbackData = await fallbackResponse.json();

            if (!fallbackData.team || !fallbackData.team.members) {
                throw new Error('Invalid shared-data.json structure');
            }

            console.log('⚠️ Using fallback data from shared-data.json');
            renderTeamCards(fallbackData.team.members, 'Cached Data (Fallback)');

        } catch (fallbackError) {
            console.error('❌ Fallback also failed:', fallbackError);
            container.innerHTML = `
                <div class="error-message" style="padding: 2rem; background: #FEE; border: 2px solid #C00; border-radius: 8px; color: #600;">
                    <h3>Unable to load team data</h3>
                    <p>Both Knowledge Graph API and fallback data source failed.</p>
                    <p><strong>Error:</strong> ${error.message}</p>
                    <p><strong>Fallback Error:</strong> ${fallbackError.message}</p>
                </div>
            `;
        }
    }
}

/**
 * Render team member cards from data
 * @param {Array} members - Array of team member objects
 * @param {string} source - Data source for debugging
 */
function renderTeamCards(members, source = 'Unknown') {
    const container = document.getElementById('team-container');

    if (!members || members.length === 0) {
        container.innerHTML = '<p class="error">No team members found</p>';
        return;
    }

    // Clear loading state
    container.innerHTML = '';

    // Add data source indicator (for transparency)
    const sourceIndicator = document.createElement('div');
    sourceIndicator.className = 'data-source-indicator';
    sourceIndicator.style.cssText = 'text-align: center; font-size: 0.85rem; color: #64748B; margin-bottom: 1rem;';
    sourceIndicator.innerHTML = `<em>Team data loaded from: <strong>${source}</strong></em>`;
    container.parentElement.insertBefore(sourceIndicator, container);

    // Create team grid
    const teamGrid = document.createElement('div');
    teamGrid.className = 'team-grid';

    // Render each team member
    members.forEach(member => {
        const card = createTeamCard(member);
        teamGrid.appendChild(card);
    });

    container.appendChild(teamGrid);

    console.log(`✅ Rendered ${members.length} team cards from ${source}`);
}

/**
 * Create a team member card element
 * @param {Object} member - Team member data
 * @returns {HTMLElement} Team card element
 */
function createTeamCard(member) {
    const card = document.createElement('div');
    card.className = 'team-card';
    card.setAttribute('data-member-id', member.id);

    // Card Header
    const header = document.createElement('div');
    header.className = 'card-header';
    header.innerHTML = `
        <h3>${escapeHtml(member.name || 'Unknown')}</h3>
        <p class="title">${escapeHtml(member.title || 'Team Member')}</p>
    `;

    // Card Body
    const body = document.createElement('div');
    body.className = 'card-body';

    // Match Score
    const matchScore = member.match_score || 0;
    body.innerHTML = `
        <div class="match-score">
            <span class="score">${matchScore}%</span>
            <span>Project Match</span>
        </div>
    `;

    // Primary Role
    if (member.primary_role) {
        const roleSection = document.createElement('div');
        roleSection.className = 'role-section';
        roleSection.innerHTML = `
            <strong>Project Role:</strong>
            <p>${escapeHtml(member.primary_role)}</p>
        `;
        body.appendChild(roleSection);
    }

    // Core Skills
    if (member.core_skills && member.core_skills.length > 0) {
        const skillsSection = document.createElement('div');
        skillsSection.className = 'role-section';
        skillsSection.innerHTML = '<strong>Core Skills:</strong>';

        const skillsList = document.createElement('ul');
        skillsList.className = 'skills-list';

        // Show top 6 skills
        member.core_skills.slice(0, 6).forEach(skill => {
            const skillTag = document.createElement('li');
            skillTag.className = 'skill-tag';
            skillTag.textContent = skill;
            skillsList.appendChild(skillTag);
        });

        skillsSection.appendChild(skillsList);
        body.appendChild(skillsSection);
    }

    // Key Achievements
    if (member.key_achievements && member.key_achievements.length > 0) {
        const achievementsSection = document.createElement('div');
        achievementsSection.className = 'role-section';
        achievementsSection.innerHTML = '<strong>Key Achievements:</strong>';

        const achievementsList = document.createElement('ul');
        achievementsList.className = 'achievements-list';

        // Show top 3 achievements
        member.key_achievements.slice(0, 3).forEach(achievement => {
            const li = document.createElement('li');

            if (typeof achievement === 'object' && achievement.description && achievement.metric) {
                li.innerHTML = `${escapeHtml(achievement.description)}: <span class="metric">${escapeHtml(achievement.metric)}</span>`;
            } else if (typeof achievement === 'string') {
                li.textContent = achievement;
            }

            achievementsList.appendChild(li);
        });

        achievementsSection.appendChild(achievementsList);
        body.appendChild(achievementsSection);
    }

    // Background Information
    const backgroundInfo = document.createElement('div');
    backgroundInfo.className = 'background-info';

    let backgroundHTML = '';

    if (member.experience_years) {
        backgroundHTML += `<p><strong>Experience:</strong> ${member.experience_years} years</p>`;
    }

    if (member.past_companies && member.past_companies.length > 0) {
        backgroundHTML += `<p><strong>Past Companies:</strong> ${member.past_companies.map(c => escapeHtml(c)).join(', ')}</p>`;
    }

    if (member.gpa) {
        backgroundHTML += `<p><strong>GPA:</strong> ${member.gpa}/4.0</p>`;
    }

    if (backgroundHTML) {
        backgroundInfo.innerHTML = backgroundHTML;
        body.appendChild(backgroundInfo);
    }

    // Assemble card
    card.appendChild(header);
    card.appendChild(body);

    return card;
}

/**
 * Escape HTML to prevent XSS
 * @param {string} text - Text to escape
 * @returns {string} Escaped text
 */
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

/**
 * Initialize on DOM ready
 */
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadTeamData);
} else {
    loadTeamData();
}
