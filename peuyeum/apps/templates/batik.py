import sys
import os

sys.path.append('../../')
from lib.cilok import urlEncode16
from lib.config import tokenuri

div_menu="""
<div class="container">
<a href="%LAMAN INDONESIA%" target="_self" class="btn btn-info" role="button">Laman Indonesia</a>
|||
<a href="%TAHUN SEBELUMNYA%" target="_self" role="button" class="btn btn-info"><<</a>
<button type="button" class="btn btn-info">%PERIODE%</button>
<a href="%TAHUN SETELAHNYA%" target="_self" role="button" class="btn btn-info">>></a>

<!-- Modal -->
<div class="modal fade" id="myModal" role="dialog">
  <div class="modal-dialog">

    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">Daftar Kunjungan per Kota/Kabupaten</h4>
      </div>
      <div class="modal-body">
        <p id="listagenda">Belum Terkunjungi.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      </div>
    </div>

  </div>
</div>


</div>
"""

div_menu_peta="""
<div class="container">
<a href="%TAHUN SEBELUMNYA%" target="_self" role="button" class="btn btn-info"><<</a>
<button type="button" class="btn btn-info">%PERIODE%</button>
<a href="%TAHUN SETELAHNYA%" target="_self" role="button" class="btn btn-info">>></a>
</div>
"""

div_map="""
<div id="map" class="map"></div>
"""

div_open_none="""
<div style="display: none;">
"""
overlay="""
<a data-toggle="modal" data-target="#myModal" class="overlay" id="%_overlay%" target="_self" href="#" onclick="listAgenda('%_kabkoturl%')">%_kabkot%</a>
"""

overlay_peta="""
<a class="overlay" id="%_overlay%" target="_self" href="%_provurl%">%_kodeprov%</a>
"""

marker="""
<div class="marker" id="%_marker%" title="Marker"></div>
"""

div_close_none="""
</div>
"""

script_open="""
<script>
"""


script_attribution="""
var logoElement = document.createElement('a');
logoElement.href = '%LAMAN INDONESIA%';
logoElement.target = '_self';

var logoImage = document.createElement('img');
logoImage.src = './favicon.ico';

logoElement.appendChild(logoImage);      

"""

script_mapsource="""
var map = new ol.Map({
  target: 'map',
  layers: [
    			new ol.layer.Tile({
      						 source: new ol.source.XYZ({
        													url: '%WMTS%'
      													})
    							 })
  		],
  view: new ol.View({
    					center: ol.proj.transform([%_centerlat_centerlong%], 'EPSG:4326', 'EPSG:3857'),
    					zoom: %_mapzoom%,
						minZoom: 5,
    					maxZoom: 19
  				}),
	logo: logoElement
	});
"""

script_zoomslider="""
zoomslider = new ol.control.ZoomSlider();
map.addControl(zoomslider);
"""



script_overlay="""
var pos = ol.proj.fromLonLat([%_lat_long%]);
var m = new ol.Overlay({
  position: pos,
  positioning: 'center-center',
  element: document.getElementById('%_marker%'),
  stopEvent: false
});
map.addOverlay(m);
var o = new ol.Overlay({
  position: pos,
  element: document.getElementById('%_overlay%'),
  stopEvent: false
});
map.addOverlay(o);
"""

script_getAgenda="""
function listAgenda(kabkot) {
	var xmlhttp = new XMLHttpRequest();
	var params = "periode=%PERIODE%";
	xmlhttp.open("POST", kabkot, false);
	xmlhttp.send(params);
    document.getElementById("listagenda").innerHTML = xmlhttp.responseText;
}
"""

script_close="""
</script>
"""
def nasional(viewname,listkodeprov,petaloc,mapzoom,provcord):
	view_path = './apps/views/'+viewname
	if not os.path.exists(view_path):
		os.makedirs(view_path)
		view_file = view_path+'/index.batik'
		if not os.path.exists(view_file):
			sys.stdout = open(view_file,'w')
			prov(listkodeprov,petaloc,mapzoom,provcord)
			sys.stdout.close()

def provinsi(viewname,listkabkot,provloc,mapzoom,kabkotcord):
	view_path = './apps/views/'+viewname
	if not os.path.exists(view_path):
		os.makedirs(view_path)
		view_file = view_path+'/index.batik'
		if not os.path.exists(view_file):
			sys.stdout = open(view_file,'w')
			kabkot(listkabkot,provloc,mapzoom,kabkotcord)
			sys.stdout.close()
			
def kabkot(kabkot,provloc,mapzoom,kabkotcord):
	print div_menu
	print div_map
	print div_open_none
	for idx,kabkotnum in enumerate(kabkot):
		urltogetdata = urlEncode16(tokenuri+'%agenda%getList'+kabkotnum[:-1])
		print overlay.replace("%_overlay%","o"+str(idx),1).replace("%_kabkoturl%",urltogetdata,1).replace("%_kabkot%",kabkotnum,1)
	for idx,kabkotnum in enumerate(kabkot):
		print marker.replace("%_marker%","m"+str(idx),1)
	print div_close_none
	print script_open
	print script_attribution
	print script_mapsource.replace('%_centerlat_centerlong%',provloc,1).replace('%_mapzoom%',mapzoom,1)
	print script_zoomslider
	for idx,kabkotloc in enumerate(kabkotcord):
		print script_overlay.replace("%_lat_long%",kabkotloc).replace("%_marker%","m"+str(idx),1).replace("%_overlay%","o"+str(idx),1)
	print script_getAgenda
	print script_close
	
def prov(listkodeprov,petaloc,mapzoom,provcord):
	print div_menu_peta
	print div_map
	print div_open_none
	for idx,kodeprov in enumerate(listkodeprov):
		print overlay_peta.replace("%_overlay%","o"+str(idx),1).replace("%_provurl%",kodeprov[:3]+' uri%',1).replace("%_kodeprov%",kodeprov,1)
	for idx,kodeprov in enumerate(listkodeprov):
		print marker.replace("%_marker%","m"+str(idx),1)
	print div_close_none
	print script_open
	print script_attribution
	print script_mapsource.replace('%_centerlat_centerlong%',petaloc,1).replace('%_mapzoom%',mapzoom,1)
	print script_zoomslider
	for idx,provloc in enumerate(provcord):
		print script_overlay.replace("%_lat_long%",provloc).replace("%_marker%","m"+str(idx),1).replace("%_overlay%","o"+str(idx),1)
	print script_close