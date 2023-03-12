const menu_button=document.querySelector(".menu_button")
    const menu_element=document.querySelector(".top_section ul")
    menu_button.addEventListener("click",function () {
        console.log("hello")
        if(menu_element.classList.contains("absolute_menu") && menu_button.classList.contains("menu_button_transfromed")) {
            menu_element.classList.remove("absolute_menu")
            menu_button.classList.remove("menu_button_transfromed")
            return
        }
        
        menu_element.classList.add("absolute_menu")
        menu_button.classList.add("menu_button_transfromed")
    })
    addEventListener("resize", (event) => {
        if(window.innerWidth>=720){
            menu_element.classList.remove("absolute_menu")
            menu_button.classList.remove("menu_button_transfromed")
        }
    });
    
                                                                                