() => {
	//getting brand
	function getBrandFromContent(content){
		return content.getElementsByClassName("cat_brandName-2XZRz cat_ellipsis-MujnT")[0].innerText;
	}
	//getting name
	function getNameFromContent(content){
		var name = content.getElementsByClassName("cat_articleName--arFp cat_ellipsis-MujnT")[0].innerText;
		name = name.replace('\'',"\\\'");
		name = name.replace('\"',"\\\"");
		return name
	}
	//getting img src
	function getImgFromContent(content){
		return content.getElementsByTagName("img")[0].src;
	}
	//getting price
	function getPriceFromContent(content){
		var price = content.getElementsByClassName("cat_originalPrice-2Oy4G")[0].innerText;
		price = price.replace(',','.');
		price = price.replace('zł','');
		price = price.replace(' ','');
		price = price.replace('od','');
		return parseFloat(price);
	}

	//getting array json
	function getJSONFromSide(){
		var x = [];
		//get list with content
		var contentList = document.getElementsByClassName("cat_card-1o_9G cat_normalWidth-tz8JR");
		//loop over content list
		for(content of contentList){
			if (typeof(content.getElementsByClassName("cat_brandName-2XZRz cat_ellipsis-MujnT")[0]) == 'undefined')
				continue;
			var JSONElem = {
				brand : getBrandFromContent(content),
				name : getNameFromContent(content),
				img : getImgFromContent(content),
				price : getPriceFromContent(content)
			};
			x.push(JSONElem);
		}
		return JSON.stringify(x)
	}

	return getJSONFromSide();
}