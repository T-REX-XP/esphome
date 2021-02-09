import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import automation
from esphome.components import cover, ble_client
from esphome.const import CONF_ID, CONF_PIN

DEPENDENCIES = ['ble_client']

am43_cover_ns = cg.esphome_ns.namespace('am43_cover')
Am43Cover = am43_cover_ns.class_('Am43Cover', cover.Cover,
                                 ble_client.BLEClientNode, cg.Component)

CONFIG_SCHEMA = cover.COVER_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(Am43Cover),
    cv.Optional(CONF_PIN, default=8888): cv.int_range(min=0, max=0xFFFF),
    }).extend(ble_client.BLE_CLIENT_SCHEMA).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add(var.set_pin(config[CONF_PIN]))
    yield cg.register_component(var, config)
    yield cover.register_cover(var, config)
    yield ble_client.register_ble_node(var, config)
