import * as functions from 'firebase-functions';

// // Start writing Firebase Functions
// // https://firebase.google.com/docs/functions/typescript
//
// export const helloWorld = functions.https.onRequest((request, response) => {
//   functions.logger.info("Hello logs!", {structuredData: true});
//   response.send("Hello from Firebase!");
// });

import * as admin from 'firebase-admin';
import * as firebaseHelper from 'firebase-functions-helper/dist';
import * as express from 'express';
import * as bodyParser from 'body-parser';

admin.initializeApp(functions.config().firebase);
const database = admin.firestore();

const app = express();
const main = express();

main.use(bodyParser.json());
main.use(bodyParser.urlencoded({extended: false}));
main.use('api/v1', app);

const deviceCollection = 'devices';
export const webApi = functions.https.onRequest(main);

app.patch('/device/:deviceId', async(req, res) =>{
    try{
      await firebaseHelper.firestore.updateDocument(database, deviceCollection, req.params.deviceId, req.body);
      res.status(200).send('Update Success');
    }catch(error){
      res.status(204).send('Patch Error')
    }
})
