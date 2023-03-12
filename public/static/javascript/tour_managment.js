// let tour_addition_selected=false
const popup_tour_container=document.querySelector(".popup_tour_container")

const add_tour_button=document.querySelector(".add")
add_tour_button.addEventListener("click",()=>{
    // tour_addition_selected=true
    tour_popup_maker()
})
document.getElementById("form_close").addEventListener("click",()=>{
    tour_popup_maker()
})

// adds from_sclae_zero to popup_tuor_container depending on tour_addtion_sleected
function tour_popup_maker() {
    if (popup_tour_container.classList.contains("form_zero_scale")){
        popup_tour_container.classList.remove("form_zero_scale")
        return
    }
    // popup_tour_container does not contains("form_zero_scale")
    popup_tour_container.classList.add("form_zero_scale")
    
}


// form managmemt

const tour_form=document.querySelector(".tour_form")
tour_form.addEventListener("submit",function (event) {
    event.preventDefault()
    const input_images=document.querySelector(".tour_input_files input")
    console.log("file",input_images)
    const Form_data=new FormData(event.target)
    for (pair of Form_data){
        console.log(pair[0],pair[1])
    }

    // send this to server to save 
})

