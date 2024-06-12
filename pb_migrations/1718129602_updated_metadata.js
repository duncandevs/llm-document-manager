/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ilnodc8xu08tbo5")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "axabixnu",
    "name": "summary",
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
  collection.schema.removeField("axabixnu")

  return dao.saveCollection(collection)
})
