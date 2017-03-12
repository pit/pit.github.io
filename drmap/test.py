import gmplot

gmap = gmplot.GoogleMapPlotter(55.647627, 37.760832, 16)

data = [
 [55.647627, 37.760832, '(1,2,4)'],
 [55.648261, 37.760275, '(2,3,4)'],
 [55.649116, 37.759151, '(4,1,1)'],
 [55.649898, 37.758368, '(1,1,1)']
]

for x in data:
  gmap.marker(x[0], x[1], title=x[2])
# gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
# gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
# gmap.heatmap(heat_lats, heat_lngs)

gmap.draw("mymap.html")