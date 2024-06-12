/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ilnodc8xu08tbo5")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "goyj9y1k",
    "name": "actors",
    "type": "json",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "maxSize": 2000000
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ilnodc8xu08tbo5")

  // remove
  collection.schema.removeField("goyj9y1k")

  return dao.saveCollection(collection)
})
