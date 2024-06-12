/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("077dbu51xebkuvs")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "wfljy0ku",
    "name": "file_name",
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
  const collection = dao.findCollectionByNameOrId("077dbu51xebkuvs")

  // remove
  collection.schema.removeField("wfljy0ku")

  return dao.saveCollection(collection)
})
