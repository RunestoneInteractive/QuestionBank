.. activecode:: menu_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: CSS
   :subchapter: advancedmatching
   :topics: CSS/advancedmatching
   :from_source: T
   :language: html

   <html>
   <head>
   <title>SubMenus</title>
   <style type='text/css'>
   body {
       background: #EEE;
       color: #000;
   }

   h1 {
       color: #AAA;
       border-bottom: 1px solid;
       margin-bottom: 0;
   }

   main {
       color: #CCC;
       margin-left: 7em;
       padding: 1px 0 1px 5%;
       border-left: 1px solid;
   }

   nav {
       float: left;
       width: 7em;
       background: #FDD;
   }

   nav ul {
        margin: 0;
        padding: 0;
        width: 7em;
        background: white;
        border: 1px solid;
   }

   nav li {
        position: relative;
        list-style: none;
        margin: 0;
        border-bottom: 1px solid #CCC;
   }

   nav ul ul {
       position: absolute;
       top: 0;
       left: 7em;
       display: block;
   }

   </style>
   </head>
   <body>

   <h1>Fundamentals of Web Programming</h1>

   <nav>
   <ul >
    <li><a href='/'>Home</a></li>
    <li><a href='#'>Syllabus</a>
     <ul>
      <li><a href='#'>Text Book</a></li>
      <li><a href='#'>Office Hours</a></li>
      <li><a href='#'>Grading Policy</a></li>
      <li><a href='#'>Learning Goals</a></li>
     </ul>
    </li>
    <li><a href='#'>Resources</a></li>
    <li><a href='#'>Publications</a>
     <ul>
      <li><a href='#'>Articles</a></li>
      <li><a href='#'>Tutorials</a>
       <ul>
        <li><a href='#'>HTML</a></li>
        <li><a href='#'>CSS</a></li>
        <li><a href='#'>SVG</a></li>
        <li><a href='#'>XML</a></li>
       </ul>
      </li>
      <li><a href='#'>Assignments</a></li>
     </ul>
    </li>
    <li><a href='#'>Contact</a></li>
   </ul>
   </nav>

   <main>
   <p>
   Lorem ipsum, dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.
    Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.
   Lorem ipsum, dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.
   Lorem ipsum, dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.

   </p>

   </main>

   </body>
   </html>