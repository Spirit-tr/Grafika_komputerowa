// horses.js
// Ładowanie koni i ich animacja w karuzeli

var horses = [];
var horsePivots = [];

/**
 * Ładuje model konia, umieszcza go w pivot grupie i dodaje do sceny.
 */
function loadHorse(x, y, z, ry, scene) {
    const loader = new THREE.GLTFLoader();
    const pivot = new THREE.Group();
    loader.load('https://threejs.org/examples/models/gltf/Horse.glb', function (gltf) {
        const horse = gltf.scene;
        horse.scale.set(0.03, 0.03, 0.03);
        horse.position.set(0, 0, 0);
        horse.rotation.y = ry || 0;

        pivot.position.set(x, y, z);
        pivot.add(horse);
        scene.add(pivot);

        horses.push(horse);
        horsePivots.push(pivot);
    });
}

/**
 * Funkcja do załadowania wszystkich koni w scenie.
 */
function loadAllHorses(scene) {
    loadHorse(11, 1, 1, 0, scene);
    loadHorse(3, 1, 11, -1, scene);
    loadHorse(4, 1, -10.5, 1.2, scene);
    loadHorse(-10, 1, 6, -2.5, scene);
    loadHorse(-9, 1, -7, -3.5, scene);
}

/**
 * Aktualizacja pozycji koni w animacji (ruch góra–dół).
 */
function animateHorses(frameNumber) {
    for (let i = 0; i < horses.length; i++) {
        let horse = horses[i];
        let t = frameNumber / 20 + i;
        horse.position.y = Math.sin(t) * 0.5;
    }
}
