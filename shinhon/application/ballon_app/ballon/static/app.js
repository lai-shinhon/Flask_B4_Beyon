document.addEventListener('alpine:init', () => {
    Alpine.data('ballon', () => ({
        init() {
            console.log(this);
        }
    }));
});

window.onload = (event) => {
    console.log(`result: ${document.getElementById("Ballon").dataset.result}`);
    let data = JSON.parse(document.getElementById("Ballon").dataset.result);
    let color = '';
    if (data.size < data.air) {
        color = 'gray'
    }
    console.log(`hello, ${data.message}`);
    gsap.to("#Ballon", {scale: data.air/100, background: color,duration: 1 });
};