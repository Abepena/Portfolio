function smoothScroll(target, duration) {
    var target = document.querySelector(target)
    var targetPosition = target.getBoundingClientRect().top - 80; // top of target div
    var startPosition = window.pageYOffset; // postion from the top of the page when the page is loaded
    var startTime = null;

    function animation(currentTime) {
        if (startTime === null) startTime = currentTime;
        var timeElapsed = currentTime - startTime
        var run = ease(timeElapsed, startPosition, targetPosition, duration)
        window.scroll(0, run)
        if (timeElapsed < duration) requestAnimationFrame(animation);

    }

    // ease function from http://gizma.com/easing/
    function ease(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t + b;
        t--; 
        return -c / 2 * (t * (t - 2) - 1) + b;
    }

    requestAnimationFrame(animation); //makes our animation loop smoothly at 60fps
}

let navigationLinks = document.querySelectorAll('.smooth-scroll')

for (let e of navigationLinks){
    let link = e.getAttribute('href');

    if (link != '#') {
        e.addEventListener('click', function(){
            smoothScroll(link, 750)
        })
    }

}