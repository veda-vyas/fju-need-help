import os
root = './'
arr = []
for item in os.listdir(root):
    if os.path.isfile(os.path.join(root, item)):
        if item.endswith('.json'):
            arr.append(item[:-5])
            print arr
            if os.path.isfile(item[:-5]+'.html') == False:
                f = open(item[:-5]+'.html','w')
                message = """<!DOCTYPE html>
          <meta charset="utf-8">
          <html lang="en">
            <head>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css">
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
                <script src="https://code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
                <script src="jquery.min.js"></script>
                <script src="jquery-ui.js"></script>
            </head>
            <style type="text/css">
                a {
                    color:#000000 !important;
                    text-decoration:none;
                  }
                  a:hover{
                    text-decoration:none;
                  }
            </style>
            <body class="container">
              <div class="row">
                <div class="col-md-8">
                  <a href="#"><h2 id="Heading"></h2></a>
                </div>
                <div class="col-md-4 text-right">
                  <br><br>
                  <a href="Course_page.html">Back to Home Page</a>
                </div>
              </div>
               <hr>
               <br>
                <div id="contentbox" style="border:1px solid black; padding:20px; height:500px; overflow-y:scroll">
                    <div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">
                        <div id="collapsible-panels">
                            <h4 class="well"><a href="#">Task Description</a></h4>  
                            <div class="well-sm">
                                <span id="taskDescription"></span><br>
                                <button class="btn btn-success upload">Submit the Solution</button>
                            </div>
                            <h4 class="well"><a href="#">Need Help</a></h4>  
                            <div id="needHelp" class="well-sm"></div>
                        </div>
                    </div>
                </div>
               <br>
            </body>
            <script type="text/javascript" src="parser.js"></script>
            <script type="text/javascript">
                $.getJSON( '"""+item+"""', function( data ) {
                  parser(data);
                });
            </script>
          </html>"""
                f.write(message)
                f.close()
            g = open('Course_page.html','w')
            message = """<!DOCTYPE html>
  <meta charset="utf-8">
  <html lang="en">
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
        <script src="https://code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
        <script src="jquery.min.js"></script>
        <script src="jquery-ui.js"></script>
    </head>
    <style type="text/css">
        a {
            color:#000000 !important;
            text-decoration:none;
          }
          a:hover{
            text-decoration:none;
          }
    </style>
    <body class="container">
    	<br>
		<table class="table table-responsive">
            <thead>
               <tr>
                 <th>S.No</th>
                 <th>Name of the Assignment</th>
               </tr>
            </thead>
            <tbody id="tbody"></tbody>
         </table>
    </body>
    <script type="text/javascript">
    var arr = """+str(arr)+"""
    for (var i=1; i<=arr.length; i++){
      $("#tbody").append('<tr> <td>'+i+')</td> <td><a href="'+arr[i-1].replace(/\s/g, "")+'.html">'+arr[i-1]+'</a></td> </tr>');
    }
   </script>
  </html>"""
            g.write(message)
            g.close()    
