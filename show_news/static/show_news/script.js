
function myFunction() {
    var x = document.getElementById("demo");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else { 
        x.className = x.className.replace(" w3-show", "");
    }
}

function select_blog(name) {
    var items = document.getElementsByClassName("alternative1");
    var items2 = document.getElementsByClassName("alternative2");
    for (i = 0; i < items.length; i++){
		if(items[i].style.display != 'none'){
	 		for (i = 0; i < items.length; i++) {
				items[i].style.display='block' 
				var children = items[i].children;
				var children2 = children[0].children;
				if (children2[1].innerHTML != name ){
					items[i].style.display='none'
				}
			}
		}
    }
    for (i = 0; i < items2.length; i++){
		if(items2[i].style.display != 'none'){
			for (i = 0; i < items2.length; i++) {
				items2[i].style.display='block' 
				var children = items2[i].children;
				var children2 = children[0].children;
				if (children2[1].innerHTML != name ){
					items2[i].style.display='none'
				}
			}
		}
    }
}

function show_authors(){
	var authors = document.getElementById("all-authors");
	if (authors.style.display === 'none') {
        	authors.style.display = 'block';
    	} else {
        	authors.style.display = 'none';
    	}
	}

function show_blogs(){
	var blogs = document.getElementById("all-blogs");
	if (blogs.style.display === 'none') {
        	blogs.style.display = 'block';
    	} else {
        	blogs.style.display = 'none';
    	}
	}

function show_alternative(){
	var items = document.getElementsByClassName("alternative1");
	var items2 = document.getElementsByClassName("alternative2");
	var count = 0
	for (i = 0; i < items.length; i++){
		if(items[i].style.display != 'none'){
	 		items2[i].style.display = 'block';
			items[i].style.display = 'none';
			count += 1;
		}
	}
	if (count>0){return;};
	for (i = 0; i < items2.length; i++){
		if(items2[i].style.display != 'none'){
			items2[i].style.display = 'none';
			items[i].style.display = 'block';
		}
	}
}

(function hide_sidenav() {
	var content = document.getElementsByClassName("content");
	if (window.innerWidth < 601){
		content[0].style.marginLeft ='0';
	}
	if (window.innerWidth > 601){
		content[0].style.marginLeft ='12.5%';
	}
	})();


