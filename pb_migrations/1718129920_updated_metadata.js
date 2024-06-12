/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ilnodc8xu08tbo5")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "m3wcp9mk",
    "name": "domain",
    "type": "text",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "iqfuotji",
    "name": "tags",
    "type": "json",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "maxSize": 2000000
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "kokebyed",
    "name": "source",
    "type": "text",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "1ubhnn2y",
    "name": "is_company_wide_doc",
    "type": "bool",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {}
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "yo2njhxd",
    "name": "file_extension",
    "type": "text",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ilnodc8xu08tbo5")

  // remove
  collection.schema.removeField("m3wcp9mk")

  // remove
  collection.schema.removeField("iqfuotji")

  // remove
  collection.schema.removeField("kokebyed")

  // remove
  collection.schema.removeField("1ubhnn2y")

  // remove
  collection.schema.removeField("yo2njhxd")

  return dao.saveCollection(collection)
})
