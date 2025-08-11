// Recipe Book JavaScript Functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    initializeFilters();
    initializeFavorites();
    initializeViewToggle();
    initializeModal();
    initializeSearch();
    
    // Initialize favorites on page load
    updateFavoritesDisplay();
});

// Favorites Management
let favorites = JSON.parse(localStorage.getItem('recipe_favorites') || '[]');

function initializeFavorites() {
    // Add click listeners to all favorite buttons
    document.addEventListener('click', function(e) {
        if (e.target.closest('.favorite-btn') || e.target.closest('.favorite-btn-large')) {
            const btn = e.target.closest('.favorite-btn') || e.target.closest('.favorite-btn-large');
            toggleFavorite(btn);
        }
        
        if (e.target.closest('.remove-favorite')) {
            const recipeId = e.target.closest('.remove-favorite').dataset.recipeId;
            removeFavorite(recipeId);
        }
    });
    
    // Update favorites display on page load
    updateFavoritesDisplay();
}

function toggleFavorite(btn) {
    const recipeId = btn.dataset.recipeId;
    const recipeTitle = btn.dataset.recipeTitle;
    const recipeUrl = btn.dataset.recipeUrl;
    const recipeImage = btn.dataset.recipeImage;
    
    const existingIndex = favorites.findIndex(fav => fav.id === recipeId);
    
    if (existingIndex > -1) {
        // Remove from favorites
        favorites.splice(existingIndex, 1);
        btn.classList.remove('favorited');
        const heart = btn.querySelector('.heart');
        if (heart) heart.textContent = '🤍';
        
        const favoriteText = btn.querySelector('.favorite-text');
        if (favoriteText) favoriteText.textContent = 'Add to Favorites';
        
        showNotification(`Removed "${recipeTitle}" from favorites`, 'removed');
    } else {
        // Add to favorites
        favorites.push({
            id: recipeId,
            title: recipeTitle,
            url: recipeUrl,
            image: recipeImage
        });
        btn.classList.add('favorited');
        const heart = btn.querySelector('.heart');
        if (heart) heart.textContent = '❤️';
        
        const favoriteText = btn.querySelector('.favorite-text');
        if (favoriteText) favoriteText.textContent = 'Remove from Favorites';
        
        showNotification(`Added "${recipeTitle}" to favorites`, 'added');
    }
    
    // Save to localStorage
    localStorage.setItem('recipe_favorites', JSON.stringify(favorites));
    updateFavoritesCount();
    updateFavoritesModal();
}

function removeFavorite(recipeId) {
    const recipe = favorites.find(fav => fav.id === recipeId);
    favorites = favorites.filter(fav => fav.id !== recipeId);
    
    // Update localStorage
    localStorage.setItem('recipe_favorites', JSON.stringify(favorites));
    
    // Update UI
    updateFavoritesCount();
    updateFavoritesModal();
    updateFavoritesDisplay();
    
    if (recipe) {
        showNotification(`Removed "${recipe.title}" from favorites`, 'removed');
    }
}

function updateFavoritesDisplay() {
    // Update favorite button states
    document.querySelectorAll('.favorite-btn, .favorite-btn-large').forEach(btn => {
        const recipeId = btn.dataset.recipeId;
        const isFavorited = favorites.some(fav => fav.id === recipeId);
        
        if (isFavorited) {
            btn.classList.add('favorited');
            const heart = btn.querySelector('.heart');
            if (heart) heart.textContent = '❤️';
            
            const favoriteText = btn.querySelector('.favorite-text');
            if (favoriteText) favoriteText.textContent = 'Remove from Favorites';
        } else {
            btn.classList.remove('favorited');
            const heart = btn.querySelector('.heart');
            if (heart) heart.textContent = '🤍';
            
            const favoriteText = btn.querySelector('.favorite-text');
            if (favoriteText) favoriteText.textContent = 'Add to Favorites';
        }
    });
    
    updateFavoritesCount();
}

function updateFavoritesCount() {
    const countElement = document.getElementById('favorites-count');
    if (countElement) {
        countElement.textContent = favorites.length;
    }
}

// Filter Functionality
function initializeFilters() {
    const categoryFilter = document.getElementById('category-filter');
    const difficultyFilter = document.getElementById('difficulty-filter');
    const sortFilter = document.getElementById('sort-filter');
    
    if (categoryFilter) categoryFilter.addEventListener('change', applyFilters);
    if (difficultyFilter) difficultyFilter.addEventListener('change', applyFilters);
    if (sortFilter) sortFilter.addEventListener('change', applyFilters);
}

function applyFilters() {
    const form = document.getElementById('search-form');
    const categoryFilter = document.getElementById('category-filter');
    const difficultyFilter = document.getElementById('difficulty-filter');
    const sortFilter = document.getElementById('sort-filter');
    
    const params = new URLSearchParams(window.location.search);
    
    // Update URL parameters
    if (categoryFilter && categoryFilter.value) {
        params.set('category', categoryFilter.value);
    } else {
        params.delete('category');
    }
    
    if (difficultyFilter && difficultyFilter.value) {
        params.set('difficulty', difficultyFilter.value);
    } else {
        params.delete('difficulty');
    }
    
    if (sortFilter && sortFilter.value) {
        params.set('sort', sortFilter.value);
    } else {
        params.delete('sort');
    }
    
    // Preserve search query
    const searchInput = document.querySelector('input[name="search"]');
    if (searchInput && searchInput.value) {
        params.set('search', searchInput.value);
    }
    
    // Redirect with new parameters
    window.location.search = params.toString();
}

// Search Functionality
function initializeSearch() {
    const searchForm = document.getElementById('search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            applyFilters();
        });
    }
}

// View Toggle Functionality
function initializeViewToggle() {
    const gridViewBtn = document.getElementById('grid-view');
    const listViewBtn = document.getElementById('list-view');
    const recipesContainer = document.getElementById('recipes-container');
    
    if (!gridViewBtn || !listViewBtn || !recipesContainer) return;
    
    // Load saved view preference
    const savedView = localStorage.getItem('recipe_view_preference') || 'grid';
    if (savedView === 'list') {
        listViewBtn.classList.add('active');
        gridViewBtn.classList.remove('active');
        recipesContainer.classList.add('list-view');
    }
    
    gridViewBtn.addEventListener('click', function() {
        gridViewBtn.classList.add('active');
        listViewBtn.classList.remove('active');
        recipesContainer.classList.remove('list-view');
        localStorage.setItem('recipe_view_preference', 'grid');
    });
    
    listViewBtn.addEventListener('click', function() {
        listViewBtn.classList.add('active');
        gridViewBtn.classList.remove('active');
        recipesContainer.classList.add('list-view');
        localStorage.setItem('recipe_view_preference', 'list');
    });
}

// Modal Functionality
function initializeModal() {
    const favoritesBtn = document.getElementById('favorites-btn');
    const favoritesModal = document.getElementById('favorites-modal');
    const closeBtn = document.getElementById('close-favorites');
    
    if (!favoritesBtn || !favoritesModal || !closeBtn) return;
    
    favoritesBtn.addEventListener('click', function() {
        updateFavoritesModal();
        favoritesModal.classList.add('active');
        document.body.style.overflow = 'hidden';
    });
    
    closeBtn.addEventListener('click', closeModal);
    
    // Close modal when clicking outside
    favoritesModal.addEventListener('click', function(e) {
        if (e.target === favoritesModal) {
            closeModal();
        }
    });
    
    // Close modal with Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && favoritesModal.classList.contains('active')) {
            closeModal();
        }
    });
}

function closeModal() {
    const favoritesModal = document.getElementById('favorites-modal');
    if (favoritesModal) {
        favoritesModal.classList.remove('active');
        document.body.style.overflow = '';
    }
}

function updateFavoritesModal() {
    const favoritesList = document.getElementById('favorites-list');
    if (!favoritesList) return;
    
    if (favorites.length === 0) {
        favoritesList.innerHTML = `
            <div class="empty-favorites">
                <div style="font-size: 3rem; margin-bottom: 20px;">🤍</div>
                <h3>No favorites yet</h3>
                <p>Start adding recipes to your favorites by clicking the heart icon!</p>
            </div>
        `;
        return;
    }
    
    favoritesList.innerHTML = favorites.map(recipe => `
        <div class="favorite-recipe-item">
            <img src="${recipe.image}" alt="${recipe.title}" class="favorite-recipe-image" 
                 onerror="this.style.display='none'">
            <div class="favorite-recipe-info">
                <a href="${recipe.url}" class="favorite-recipe-title">${recipe.title}</a>
                <button class="remove-favorite" data-recipe-id="${recipe.id}">
                    Remove
                </button>
            </div>
        </div>
    `).join('');
}

// Notification System
function showNotification(message, type = 'info') {
    // Remove existing notification if any
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <span class="notification-message">${message}</span>
            <button class="notification-close" onclick="this.parentElement.parentElement.remove()">&times;</button>
        </div>
    `;
    
    // Add styles
    const styles = {
        position: 'fixed',
        top: '20px',
        right: '20px',
        background: type === 'added' ? '#27ae60' : type === 'removed' ? '#e74c3c' : '#3498db',
        color: 'white',
        padding: '15px 20px',
        borderRadius: '8px',
        boxShadow: '0 4px 20px rgba(0, 0, 0, 0.15)',
        zIndex: '1001',
        maxWidth: '300px',
        transform: 'translateX(100%)',
        transition: 'transform 0.3s ease',
        fontSize: '0.9rem'
    };
    
    Object.assign(notification.style, styles);
    
    const contentStyles = {
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        gap: '15px'
    };
    
    Object.assign(notification.querySelector('.notification-content').style, contentStyles);
    
    const closeButtonStyles = {
        background: 'none',
        border: 'none',
        color: 'white',
        fontSize: '1.2rem',
        cursor: 'pointer',
        padding: '0',
        lineHeight: '1'
    };
    
    Object.assign(notification.querySelector('.notification-close').style, closeButtonStyles);
    
    // Add to DOM
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Auto remove after 3 seconds
    setTimeout(() => {
        if (notification.parentElement) {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => {
                if (notification.parentElement) {
                    notification.remove();
                }
            }, 300);
        }
    }, 3000);
}

// Smooth scrolling for anchor links
document.addEventListener('click', function(e) {
    if (e.target.matches('a[href^="#"]')) {
        e.preventDefault();
        const targetId = e.target.getAttribute('href').slice(1);
        const targetElement = document.getElementById(targetId);
        
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    }
});

// Lazy loading for images
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Back to top functionality
function createBackToTopButton() {
    const button = document.createElement('button');
    button.innerHTML = '↑';
    button.className = 'back-to-top';
    button.title = 'Back to top';
    
    const styles = {
        position: 'fixed',
        bottom: '30px',
        right: '30px',
        width: '50px',
        height: '50px',
        background: 'var(--primary-color)',
        color: 'white',
        border: 'none',
        borderRadius: '50%',
        cursor: 'pointer',
        fontSize: '1.5rem',
        display: 'none',
        zIndex: '100',
        transition: 'all 0.3s ease',
        boxShadow: '0 4px 15px rgba(0, 0, 0, 0.2)'
    };
    
    Object.assign(button.style, styles);
    
    button.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            button.style.display = 'block';
        } else {
            button.style.display = 'none';
        }
    });
    
    document.body.appendChild(button);
}

// Initialize back to top button
createBackToTopButton();

// Recipe card hover effects
document.addEventListener('mouseover', function(e) {
    if (e.target.closest('.recipe-card')) {
        const card = e.target.closest('.recipe-card');
        card.style.transform = 'translateY(-8px)';
    }
});

document.addEventListener('mouseout', function(e) {
    if (e.target.closest('.recipe-card')) {
        const card = e.target.closest('.recipe-card');
        card.style.transform = 'translateY(0)';
    }
});