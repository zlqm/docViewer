########
showDoc
########

``showDoc`` is a small tool to help you write document.


Features
########

- render source markup to html
- live preview while editing


Current support following markup language:

  - reStructuredText
  - plantuml


Usage
#####

Command Line
*************

- render doc to html file
  * ``renderDoc``
  * ``python -m showDoc render``
- live preview doc 
  * ``previewDoc``
  * ``python -m showDoc preview``


Vim Plugin
***********

1. Install the plugin

   ``Plug 'zlqm/showDoc', { 'rtp': 'plugins/vim' }``

2. Editing a rst file and run command

   ``:LivePreview``




Demo
*****

Just run this command and you can preview the doc in browser::

  showDoc ) previewDoc demo.rst
  Start preview server [debug: False] bind to localhost:9000
  visit http://localhost:9000/lite-preview?filename=demo.rst to preview
