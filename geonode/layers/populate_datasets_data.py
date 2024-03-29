#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################
from django.conf import settings
from django.contrib.auth import get_user_model

from geonode.layers.models import Style, Attribute, Dataset

ogc_location = settings.OGC_SERVER['default']['LOCATION']


styles = [{"name": "test_style_1",
           "sld_url": f"{ogc_location}rest/styles/test_style.sld",
           "sld_body": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><sld:StyledLayerDescriptor \
            xmlns=\"http://www.opengis.net/sld\" xmlns:sld=\"http://www.opengis.net/sld\" \
            xmlns:ogc=\"http://www.opengis.net/ogc\" xmlns:gml=\"http://www.opengis.net/gml\" \
            version=\"1.0.0\"><sld:NamedLayer><sld:Name>test_style_1</sld:Name><sld:UserStyle>\
            <sld:Name>test_style_1</sld:Name><sld:Title/><sld:FeatureTypeStyle><sld:Name>name</sld:Name>\
            <sld:Rule><sld:PolygonSymbolizer><sld:Fill><sld:CssParameter name=\"fill\">#888800</sld:CssParameter>\
            </sld:Fill><sld:Stroke><sld:CssParameter name=\"stroke\">#ffffbb</sld:CssParameter>\
            <sld:CssParameter name=\"stroke-width\">0.7</sld:CssParameter></sld:Stroke>\
            </sld:PolygonSymbolizer></sld:Rule></sld:FeatureTypeStyle></sld:UserStyle>\
            </sld:NamedLayer></sld:StyledLayerDescriptor>",
           },
          {"name": "test_style_2",
           "sld_url": f"{ogc_location}rest/styles/test_style.sld",
           "sld_body": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><sld:StyledLayerDescriptor \
           xmlns=\"http://www.opengis.net/sld\" xmlns:sld=\"http://www.opengis.net/sld\" \
           xmlns:ogc=\"http://www.opengis.net/ogc\" xmlns:gml=\"http://www.opengis.net/gml\" \
           version=\"1.0.0\"><sld:NamedLayer><sld:Name>test_style_2</sld:Name><sld:UserStyle>\
           <sld:Name>test_style_2</sld:Name><sld:Title/><sld:FeatureTypeStyle><sld:Name>name</sld:Name>\
           <sld:Rule><sld:PolygonSymbolizer><sld:Fill><sld:CssParameter name=\"fill\">#888800</sld:CssParameter>\
           </sld:Fill><sld:Stroke><sld:CssParameter name=\"stroke\">#ffffbb</sld:CssParameter>\
           <sld:CssParameter name=\"stroke-width\">0.7</sld:CssParameter></sld:Stroke></sld:PolygonSymbolizer>\
           </sld:Rule></sld:FeatureTypeStyle></sld:UserStyle></sld:NamedLayer></sld:StyledLayerDescriptor>",
           },
          {"name": "test_style_3",
           "sld_url": f"{ogc_location}rest/styles/test_style.sld",
           "sld_body": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><sld:StyledLayerDescriptor \
           xmlns=\"http://www.opengis.net/sld\" xmlns:sld=\"http://www.opengis.net/sld\" \
           xmlns:ogc=\"http://www.opengis.net/ogc\" xmlns:gml=\"http://www.opengis.net/gml\" \
           version=\"1.0.0\"><sld:NamedLayer><sld:Name>test_style_3</sld:Name><sld:UserStyle>\
           <sld:Name>test_style_3</sld:Name><sld:Title/><sld:FeatureTypeStyle><sld:Name>name</sld:Name>\
           <sld:Rule><sld:PolygonSymbolizer><sld:Fill><sld:CssParameter name=\"fill\">#888800</sld:CssParameter>\
           </sld:Fill><sld:Stroke><sld:CssParameter name=\"stroke\">#ffffbb</sld:CssParameter><sld:CssParameter \
           name=\"stroke-width\">0.7</sld:CssParameter></sld:Stroke></sld:PolygonSymbolizer></sld:Rule>\
           </sld:FeatureTypeStyle></sld:UserStyle></sld:NamedLayer></sld:StyledLayerDescriptor>",
           },
          {"name": "Evaluación",
           "sld_url": f"{ogc_location}rest/styles/test_style.sld",
           "sld_body": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><sld:StyledLayerDescriptor \
           xmlns=\"http://www.opengis.net/sld\" xmlns:sld=\"http://www.opengis.net/sld\" \
           xmlns:ogc=\"http://www.opengis.net/ogc\" xmlns:gml=\"http://www.opengis.net/gml\" version=\"1.0.0\">\
           <sld:NamedLayer><sld:Name>test_style_3</sld:Name><sld:UserStyle><sld:Name>test_style_3</sld:Name>\
           <sld:Title/><sld:FeatureTypeStyle><sld:Name>name</sld:Name><sld:Rule><sld:PolygonSymbolizer><sld:Fill>\
           <sld:CssParameter name=\"fill\">#888800</sld:CssParameter></sld:Fill><sld:Stroke><sld:CssParameter \
           name=\"stroke\">#ffffbb</sld:CssParameter><sld:CssParameter name=\"stroke-width\">0.7</sld:CssParameter>\
           </sld:Stroke></sld:PolygonSymbolizer></sld:Rule></sld:FeatureTypeStyle></sld:UserStyle></sld:NamedLayer>\
           </sld:StyledLayerDescriptor>",
           }]

attributes = [
    {
        "attribute": 'N\xfamero_De_M\xe9dicos',
        "attribute_label": 'N\xfamero_De_M\xe9dicos',
        "attribute_type": "xsd:string",
        "visible": True,
        "display_order": 4
    },
    {
        "attribute": "the_geom",
        "attribute_label": "Shape",
        "attribute_type": "gml:Geometry",
        "visible": False,
        "display_order": 3
    },
    {
        "attribute": "description",
        "attribute_label": "Description",
        "attribute_type": "xsd:string",
        "visible": True,
        "display_order": 2
    },
    {
        "attribute": "place_name",
        "attribute_label": "Place Name",
        "attribute_type": "xsd:string",
        "visible": True,
        "display_order": 1
    }
]


def create_dataset_data(object_id=None, owner=None):
    layer = Dataset.objects.get(pk=object_id) if object_id else\
        Dataset.objects.all().first()
    if not owner:
        owner = get_user_model().objects.get(username="admin")
    for style in styles:
        new_style, created = Style.objects.get_or_create(
            name=style['name'],
            defaults=dict(
                sld_url=style['sld_url'],
                sld_body=style['sld_body']))
        if new_style not in layer.styles.all():
            layer.styles.add(new_style)
            layer.default_style = new_style
    layer.owner = owner
    layer.save()

    for attr in attributes:
        Attribute.objects.update_or_create(
            dataset=layer,
            attribute=attr['attribute'],
            attribute_label=attr['attribute_label'],
            attribute_type=attr['attribute_type'],
            visible=attr['visible'],
            display_order=attr['display_order']
        )
