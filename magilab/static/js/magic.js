document.addEventListener('DOMContentLoaded', () => {
    // Création d'étincelles magiques
    function createSparkles() {
        const sparkles = document.createElement('div');
        sparkles.className = 'sparkles';
        
        for (let i = 0; i < 50; i++) {
            const sparkle = document.createElement('div');
            sparkle.className = 'sparkle';
            sparkle.style.left = `${Math.random() * 100}%`;
            sparkle.style.animationDelay = `${Math.random() * 2}s`;
            sparkles.appendChild(sparkle);
        }
        
        document.body.appendChild(sparkles);
    }
    
    // Animation au survol des boutons
    document.querySelectorAll('.btn-magic').forEach(btn => {
        btn.addEventListener('mouseover', () => {
            btn.style.transform = `scale(1.1) rotate(${Math.random() * 6 - 3}deg)`;
        });
        
        btn.addEventListener('mouseout', () => {
            btn.style.transform = 'scale(1) rotate(0deg)';
        });
    });
    
    createSparkles();
});