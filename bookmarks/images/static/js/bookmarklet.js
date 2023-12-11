const siteUrl = '//127.0.0.1:8000/';
const styleUrl = siteUrl + 'static/css/bookmarklet.css';
const minWidth = 250;
const minHeight = 250;

// Loading CSS
var head = document.getElementsByTagName('head')[0];
var link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = styleUrl + '?r=' + Math.floor(Math.random() * 9999999999999999);
head.appendChild(link);

// Load HTML
var body = document.getElementsByTagName('body')[0];
var boxHtml = `
    <div id="bookmarklet">
        <a href="#" id="close">&times;</a>
        <h1>Select an Image to bookmark:</h1>
        <div class="images"></div>
    </div>
`;

body.innerHTML += boxHtml;

// Bookmarklet main container is retrieved by getting the DOM element with ID bookmarklet with document.getElementById
function bookmarkletLaunch() {
    var bookmarklet = document.getElementById('bookmarklet');
    var imagesFound = bookmarklet.querySelector('.images');

    // Clear images found
    imagesFound.innerHTML = '';
    // Display bookmarklet
    bookmarklet.style.display = 'block';

    // Close event
    bookmarklet.querySelector('#close').addEventListener('click', function () {
        bookmarklet.style.display = 'none';
    });
}

// Calling bookmarkletLaunch()
bookmarkletLaunch();

// Function to find images in DOM with minimum dimensions
var images = document.querySelectorAll('img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"]');
images.forEach(image => {
    if (image.naturalWidth >= minWidth && image.naturalHeight >= minHeight) {
        var imagesFound = document.createElement('img');
        imagesFound.src = image.src;
        document.querySelector('.images').appendChild(imagesFound);
    }
});

// Calling bookmarkletLaunch() again (not sure why it's called twice in your code)
bookmarkletLaunch();
