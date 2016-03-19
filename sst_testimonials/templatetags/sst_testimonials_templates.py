from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def get_testimonials():
    return mark_safe("""<hr />
<table><tr><td>
<div id="cbp-qtrotator" class="cbp-qtrotator">

<div class="cbp-qtcontent current"> 
<blockquote>
<p>Quote 1</p>
<footer>Author 1</footer>
</blockquote>
</div>

<div class="cbp-qtcontent"> 
<blockquote>
<p>Quote 2</p>
<footer>Author 2</footer>
</blockquote>
</div>

<div class="cbp-qtcontent">
<blockquote>
<p>Quote 3</p>
<footer>Author 3</footer>
</blockquote>
</div>

<span class="cbp-qtprogress"></span>
</div>
</td></tr></table>
<br />
<hr />

<script type="text/javascript">
$(document).ready(function() {
//Quotes rotator
var divs = $('.cbp-qtcontent');

function fade() {
var current = $('.current');
var currentIndex = divs.index(current),
nextIndex = currentIndex + 1;

if (nextIndex >= divs.length) {
nextIndex = 0;
}

var next = divs.eq(nextIndex);

next.stop().fadeIn(1500, function() {
$(this).addClass('current');
});

current.stop().fadeOut(1500, function() {
$(this).removeClass('current');
_startProgress()
setTimeout(fade, 8000);
});
}

function _startProgress(){
$(".cbp-qtprogress").removeAttr('style');
$(".cbp-qtprogress").animate({
width:"800px",
} , 8000);
}

_startProgress()
setTimeout(fade, 8000);
});
</script>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>""")

