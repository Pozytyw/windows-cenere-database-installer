() => {
	//output list
	var list = [];
	
	//get list of elem in navi
	var contents = document.getElementsByClassName("cat_item-z_SDi")[0];
	contents = contents.getElementsByClassName("cat_item-z_SDi");
	
	for(elem of contents){
		x = [];
		x.push(elem.getElementsByTagName("a")[0].href);
		x.push(elem.innerText);
		
		list.push(x);
	}
	
	return list;
}