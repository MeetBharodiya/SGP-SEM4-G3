var noti = document.querySelector('h5');
	var select = document.querySelector('.select');
	var button = document.getElementsByClassName('add-to-cart');
	for(var but of button){
		but.addEventListener('click', (e)=>{
			var add = Number(noti.getAttribute('data-count') || 0);
			noti.setAttribute('data-count', add +1);
			noti.classList.add('zero')


			// copy and paste //
			var parent = e.target.parentNode;
			var clone = parent.cloneNode(true);
			select.appendChild(clone);
			clone.lastElementChild.innerText = "Buy-now";
			
			if (clone) {
				noti.onclick = ()=>{
					select.classList.toggle('display');
				}	
			}
		})
	}