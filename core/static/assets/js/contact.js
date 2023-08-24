jQuery(document).ready(function(){
  jQuery('#contact-form').on('submit',function(e) {  //Don't foget to change the id form
  jQuery.ajax({
      url:'contact.php', //===PHP file name====
      data:jQuery(this).serialize(),
      type:'POST',
      success:function(data){
          jQuery( ".inner-response" ).append( "<p class='alert alert-success'>Thank You! Your request has been submitted successfully. We will contact to you soon.</p>" );
          jQuery('#contact-form')[0].reset();
        
      },
      error:function(data){

         jQuery( ".inner-response" ).append( "<p class='alert alert-info'>Sorry! There is some error to send your message.</p>" );
          jQuery('#contact-form')[0].reset();
      },
  
    });
    e.preventDefault(); //This is to Avoid Page Refresh and Fire the Event "Click"
  });

});