
function dropdown() {
    var menu = document.getElementById("demo");
    if (menu.className.indexOf("w3-show") == -1) {
        menu.className += " w3-show";
    } else { 
        menu.className = menu.className.replace(" w3-show", "");
    }
}

function select_blog(name) {	
    var items = document.getElementsByClassName("alternative1");
    var items2 = document.getElementsByClassName("alternative2");
    if (name == 'show all'){
	 if(check_display()=='alternative1'){
	 	for (i = 0; i < items.length; i++) {
				items[i].style.display='block';
		}
	}
	 else {
		for (i = 0; i < items2.length; i++) {
				items2[i].style.display='block';
		}
	}
    }
    else {
	if(check_display()=='alternative1'){	
    		for (i = 0; i < items.length; i++){
			items[i].style.display='block'; 
			var children = items[i].children;
			var children2 = children[0].children;
			if (children2[1].innerHTML != name ){
				items[i].style.display='none'
			}
		}
	}
	else {
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
	dropdown();
}

function show_blogs(){
	var blogs = document.getElementById("all-blogs");
	if (blogs.style.display === 'none') {
        	blogs.style.display = 'block';
    	} else {
        	blogs.style.display = 'none';
    	}
	dropdown();
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
	dropdown();
	if (count>0){
		change_content("details", "hide details");
		return;
	};
	for (i = 0; i < items2.length; i++){
		if(items2[i].style.display != 'none'){
			items2[i].style.display = 'none';
			items[i].style.display = 'block';
		}
	}
	change_content("details", "show details");

}
function check_display(){
	var items = document.getElementsByClassName("alternative1");
	var items2 = document.getElementsByClassName("alternative2");
	var count = 0
	for (i = 0; i < items.length; i++){
		if(items[i].style.display != 'none'){
			return 'alternative1'
		}
	}
	for (i = 0; i < items2.length; i++){
		if(items2[i].style.display != 'none'){
			return 'alternative2'
		}
	}
}

function change_content(classname, content){
	var items = document.getElementsByClassName(classname);
	for ( i = 0; i < items.length; i++){
		items[i].innerHTML = content;
	}
}

function hide_sidenav() {
	var content = document.getElementById("content");
	if (window.innerWidth < 601){
		content.style.marginLeft ='0';
		show_alternative();
		dropdown();
	}
	if (window.innerWidth > 601){
		content.style.marginLeft ='12.5%';
	}
}

(hide_sidenav());

