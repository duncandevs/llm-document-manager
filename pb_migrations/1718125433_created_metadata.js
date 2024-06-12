/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "ilnodc8xu08tbo5",
    "created": "2024-06-11 17:03:53.337Z",
    "updated": "2024-06-11 17:03:53.337Z",
    "name": "metadata",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "mavfrtah",
        "name": "document_id",
        "type": "relation",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "collectionId": "077dbu51xebkuvs",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": null
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("ilnodc8xu08tbo5");

  return dao.deleteCollection(collection);
})
