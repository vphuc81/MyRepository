.class Lcom/aces/tv/Splash$DownloadObb;
.super Landroid/os/AsyncTask;
.source "Splash.java"


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/aces/tv/Splash;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x2
    name = "DownloadObb"
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Landroid/os/AsyncTask",
        "<",
        "Ljava/lang/String;",
        "Ljava/lang/Integer;",
        "Ljava/lang/Integer;",
        ">;"
    }
.end annotation


# instance fields
.field private mProgressStatus:I

.field private mSplash:Lcom/aces/tv/Splash;

.field final synthetic this$0:Lcom/aces/tv/Splash;


# direct methods
.method public constructor <init>(Lcom/aces/tv/Splash;Lcom/aces/tv/Splash;)V
    .locals 1

    .prologue
    .line 166
    iput-object p1, p0, Lcom/aces/tv/Splash$DownloadObb;->this$0:Lcom/aces/tv/Splash;

    invoke-direct {p0}, Landroid/os/AsyncTask;-><init>()V

    .line 163
    const/4 v0, 0x0

    iput-object v0, p0, Lcom/aces/tv/Splash$DownloadObb;->mSplash:Lcom/aces/tv/Splash;

    .line 164
    const/4 v0, 0x0

    iput v0, p0, Lcom/aces/tv/Splash$DownloadObb;->mProgressStatus:I

    .line 167
    iput-object p2, p0, Lcom/aces/tv/Splash$DownloadObb;->mSplash:Lcom/aces/tv/Splash;

    .line 168
    return-void
.end method


# virtual methods
.method protected varargs doInBackground([Ljava/lang/String;)Ljava/lang/Integer;
    .locals 14

    .prologue
    .line 172
    const/4 v3, 0x0

    .line 173
    const/4 v2, 0x0

    .line 174
    const/4 v1, 0x0

    .line 176
    const/4 v0, 0x0

    aget-object v0, p1, v0

    .line 177
    const/4 v4, 0x1

    aget-object v5, p1, v4

    .line 178
    new-instance v8, Ljava/io/File;

    invoke-direct {v8, v5}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    .line 180
    const-string v4, "Kodi"

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "Downloading "

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v7, " to "

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v4, v6}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 182
    invoke-virtual {v8}, Ljava/io/File;->getParentFile()Ljava/io/File;

    move-result-object v4

    invoke-virtual {v4}, Ljava/io/File;->exists()Z

    move-result v4

    if-nez v4, :cond_1

    invoke-virtual {v8}, Ljava/io/File;->getParentFile()Ljava/io/File;

    move-result-object v4

    invoke-virtual {v4}, Ljava/io/File;->mkdirs()Z

    move-result v4

    if-nez v4, :cond_1

    .line 183
    const-string v0, "Kodi"

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "Error creating directory "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v8}, Ljava/io/File;->getParentFile()Ljava/io/File;

    move-result-object v2

    invoke-virtual {v2}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    .line 184
    const/4 v0, -0x1

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    .line 244
    :cond_0
    :goto_0
    return-object v0

    .line 187
    :cond_1
    const/4 v4, 0x0

    .line 189
    :try_start_0
    new-instance v6, Ljava/net/URL;

    invoke-direct {v6, v0}, Ljava/net/URL;-><init>(Ljava/lang/String;)V

    .line 190
    invoke-virtual {v6}, Ljava/net/URL;->openConnection()Ljava/net/URLConnection;

    move-result-object v0

    check-cast v0, Ljava/net/HttpURLConnection;
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_3
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    .line 191
    :try_start_1
    invoke-virtual {v0}, Ljava/net/HttpURLConnection;->connect()V

    .line 195
    invoke-virtual {v0}, Ljava/net/HttpURLConnection;->getResponseCode()I

    move-result v1

    const/16 v6, 0xc8

    if-eq v1, v6, :cond_5

    .line 196
    const/4 v1, -0x1

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;
    :try_end_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_4
    .catchall {:try_start_1 .. :try_end_1} :catchall_1

    move-result-object v1

    .line 228
    if-eqz v2, :cond_2

    .line 229
    :try_start_2
    invoke-virtual {v2}, Ljava/io/OutputStream;->close()V

    .line 230
    :cond_2
    if-eqz v3, :cond_3

    .line 231
    invoke-virtual {v3}, Ljava/io/InputStream;->close()V
    :try_end_2
    .catch Ljava/io/IOException; {:try_start_2 .. :try_end_2} :catch_6

    .line 235
    :cond_3
    :goto_1
    if-eqz v0, :cond_4

    .line 236
    invoke-virtual {v0}, Ljava/net/HttpURLConnection;->disconnect()V

    :cond_4
    move-object v0, v1

    goto :goto_0

    .line 201
    :cond_5
    :try_start_3
    invoke-virtual {v0}, Ljava/net/HttpURLConnection;->getContentLength()I

    move-result v9

    .line 204
    invoke-virtual {v0}, Ljava/net/HttpURLConnection;->getInputStream()Ljava/io/InputStream;

    move-result-object v3

    .line 205
    new-instance v1, Ljava/io/FileOutputStream;

    invoke-direct {v1, v5}, Ljava/io/FileOutputStream;-><init>(Ljava/lang/String;)V
    :try_end_3
    .catch Ljava/lang/Exception; {:try_start_3 .. :try_end_3} :catch_4
    .catchall {:try_start_3 .. :try_end_3} :catchall_1

    .line 207
    const/16 v2, 0x1000

    :try_start_4
    new-array v2, v2, [B

    .line 208
    const-wide/16 v6, 0x0

    .line 210
    iget-object v5, p0, Lcom/aces/tv/Splash$DownloadObb;->this$0:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mProgress:Landroid/widget/ProgressBar;
    invoke-static {v5}, Lcom/aces/tv/Splash;->access$300(Lcom/aces/tv/Splash;)Landroid/widget/ProgressBar;

    move-result-object v5

    const/4 v10, 0x0

    invoke-virtual {v5, v10}, Landroid/widget/ProgressBar;->setProgress(I)V

    .line 211
    iget-object v5, p0, Lcom/aces/tv/Splash$DownloadObb;->this$0:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mProgress:Landroid/widget/ProgressBar;
    invoke-static {v5}, Lcom/aces/tv/Splash;->access$300(Lcom/aces/tv/Splash;)Landroid/widget/ProgressBar;

    move-result-object v5

    invoke-virtual {v5, v9}, Landroid/widget/ProgressBar;->setMax(I)V

    .line 212
    :goto_2
    invoke-virtual {v3, v2}, Ljava/io/InputStream;->read([B)I

    move-result v5

    const/4 v10, -0x1

    if-eq v5, v10, :cond_11

    .line 214
    invoke-virtual {p0}, Lcom/aces/tv/Splash$DownloadObb;->isCancelled()Z
    :try_end_4
    .catch Ljava/lang/Exception; {:try_start_4 .. :try_end_4} :catch_0
    .catchall {:try_start_4 .. :try_end_4} :catchall_2

    move-result v10

    if-eqz v10, :cond_9

    .line 215
    const/4 v2, -0x1

    .line 228
    :goto_3
    if-eqz v1, :cond_6

    .line 229
    :try_start_5
    invoke-virtual {v1}, Ljava/io/OutputStream;->close()V

    .line 230
    :cond_6
    if-eqz v3, :cond_7

    .line 231
    invoke-virtual {v3}, Ljava/io/InputStream;->close()V
    :try_end_5
    .catch Ljava/io/IOException; {:try_start_5 .. :try_end_5} :catch_5

    .line 235
    :cond_7
    :goto_4
    if-eqz v0, :cond_8

    .line 236
    invoke-virtual {v0}, Ljava/net/HttpURLConnection;->disconnect()V

    .line 238
    :cond_8
    if-nez v2, :cond_10

    .line 239
    iget-object v0, p0, Lcom/aces/tv/Splash$DownloadObb;->this$0:Lcom/aces/tv/Splash;

    const/16 v1, 0x5b

    # setter for: Lcom/aces/tv/Splash;->mState:I
    invoke-static {v0, v1}, Lcom/aces/tv/Splash;->access$002(Lcom/aces/tv/Splash;I)I

    .line 243
    :goto_5
    const/4 v0, 0x1

    new-array v0, v0, [Ljava/lang/Integer;

    const/4 v1, 0x0

    const/4 v3, 0x0

    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    aput-object v3, v0, v1

    invoke-virtual {p0, v0}, Lcom/aces/tv/Splash$DownloadObb;->publishProgress([Ljava/lang/Object;)V

    .line 244
    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto/16 :goto_0

    .line 218
    :cond_9
    int-to-long v10, v5

    add-long/2addr v6, v10

    .line 220
    if-lez v9, :cond_a

    .line 221
    const/4 v10, 0x1

    :try_start_6
    new-array v10, v10, [Ljava/lang/Integer;

    const/4 v11, 0x0

    long-to-int v12, v6

    invoke-static {v12}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v12

    aput-object v12, v10, v11

    invoke-virtual {p0, v10}, Lcom/aces/tv/Splash$DownloadObb;->publishProgress([Ljava/lang/Object;)V

    .line 222
    :cond_a
    const/4 v10, 0x0

    invoke-virtual {v1, v2, v10, v5}, Ljava/io/OutputStream;->write([BII)V
    :try_end_6
    .catch Ljava/lang/Exception; {:try_start_6 .. :try_end_6} :catch_0
    .catchall {:try_start_6 .. :try_end_6} :catchall_2

    goto :goto_2

    .line 224
    :catch_0
    move-exception v2

    move-object v2, v1

    move-object v1, v0

    .line 225
    :goto_6
    const/4 v0, -0x1

    :try_start_7
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;
    :try_end_7
    .catchall {:try_start_7 .. :try_end_7} :catchall_0

    move-result-object v0

    .line 228
    if-eqz v2, :cond_b

    .line 229
    :try_start_8
    invoke-virtual {v2}, Ljava/io/OutputStream;->close()V

    .line 230
    :cond_b
    if-eqz v3, :cond_c

    .line 231
    invoke-virtual {v3}, Ljava/io/InputStream;->close()V
    :try_end_8
    .catch Ljava/io/IOException; {:try_start_8 .. :try_end_8} :catch_2

    .line 235
    :cond_c
    :goto_7
    if-eqz v1, :cond_0

    .line 236
    invoke-virtual {v1}, Ljava/net/HttpURLConnection;->disconnect()V

    goto/16 :goto_0

    .line 227
    :catchall_0
    move-exception v0

    .line 228
    :goto_8
    if-eqz v2, :cond_d

    .line 229
    :try_start_9
    invoke-virtual {v2}, Ljava/io/OutputStream;->close()V

    .line 230
    :cond_d
    if-eqz v3, :cond_e

    .line 231
    invoke-virtual {v3}, Ljava/io/InputStream;->close()V
    :try_end_9
    .catch Ljava/io/IOException; {:try_start_9 .. :try_end_9} :catch_1

    .line 235
    :cond_e
    :goto_9
    if-eqz v1, :cond_f

    .line 236
    invoke-virtual {v1}, Ljava/net/HttpURLConnection;->disconnect()V

    :cond_f
    throw v0

    .line 241
    :cond_10
    invoke-virtual {v8}, Ljava/io/File;->delete()Z

    goto :goto_5

    .line 232
    :catch_1
    move-exception v2

    goto :goto_9

    .line 227
    :catchall_1
    move-exception v1

    move-object v13, v1

    move-object v1, v0

    move-object v0, v13

    goto :goto_8

    :catchall_2
    move-exception v2

    move-object v13, v2

    move-object v2, v1

    move-object v1, v0

    move-object v0, v13

    goto :goto_8

    .line 232
    :catch_2
    move-exception v2

    goto :goto_7

    .line 224
    :catch_3
    move-exception v0

    goto :goto_6

    :catch_4
    move-exception v1

    move-object v1, v0

    goto :goto_6

    .line 232
    :catch_5
    move-exception v1

    goto :goto_4

    :catch_6
    move-exception v2

    goto/16 :goto_1

    :cond_11
    move v2, v4

    goto/16 :goto_3
.end method

.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;
    .locals 1

    .prologue
    .line 161
    check-cast p1, [Ljava/lang/String;

    invoke-virtual {p0, p1}, Lcom/aces/tv/Splash$DownloadObb;->doInBackground([Ljava/lang/String;)Ljava/lang/Integer;

    move-result-object v0

    return-object v0
.end method

.method protected onPostExecute(Ljava/lang/Integer;)V
    .locals 2

    .prologue
    .line 263
    invoke-super {p0, p1}, Landroid/os/AsyncTask;->onPostExecute(Ljava/lang/Object;)V

    .line 264
    invoke-virtual {p1}, Ljava/lang/Integer;->intValue()I

    move-result v0

    if-gez v0, :cond_0

    .line 265
    iget-object v0, p0, Lcom/aces/tv/Splash$DownloadObb;->this$0:Lcom/aces/tv/Splash;

    const/4 v1, 0x1

    # setter for: Lcom/aces/tv/Splash;->mState:I
    invoke-static {v0, v1}, Lcom/aces/tv/Splash;->access$002(Lcom/aces/tv/Splash;I)I

    .line 266
    iget-object v0, p0, Lcom/aces/tv/Splash$DownloadObb;->this$0:Lcom/aces/tv/Splash;

    const-string v1, "Cannot download obb."

    # setter for: Lcom/aces/tv/Splash;->mErrorMsg:Ljava/lang/String;
    invoke-static {v0, v1}, Lcom/aces/tv/Splash;->access$102(Lcom/aces/tv/Splash;Ljava/lang/String;)Ljava/lang/String;

    .line 269
    :cond_0
    iget-object v0, p0, Lcom/aces/tv/Splash$DownloadObb;->this$0:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mStateMachine:Lcom/aces/tv/Splash$StateMachine;
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$1000(Lcom/aces/tv/Splash;)Lcom/aces/tv/Splash$StateMachine;

    move-result-object v0

    iget-object v1, p0, Lcom/aces/tv/Splash$DownloadObb;->this$0:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mState:I
    invoke-static {v1}, Lcom/aces/tv/Splash;->access$000(Lcom/aces/tv/Splash;)I

    move-result v1

    invoke-virtual {v0, v1}, Lcom/aces/tv/Splash$StateMachine;->sendEmptyMessage(I)Z

    .line 270
    return-void
.end method

.method protected bridge synthetic onPostExecute(Ljava/lang/Object;)V
    .locals 0

    .prologue
    .line 161
    check-cast p1, Ljava/lang/Integer;

    invoke-virtual {p0, p1}, Lcom/aces/tv/Splash$DownloadObb;->onPostExecute(Ljava/lang/Integer;)V

    return-void
.end method

.method protected varargs onProgressUpdate([Ljava/lang/Integer;)V
    .locals 3

    .prologue
    const/4 v2, 0x0

    .line 249
    iget-object v0, p0, Lcom/aces/tv/Splash$DownloadObb;->this$0:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mState:I
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$000(Lcom/aces/tv/Splash;)I

    move-result v0

    packed-switch v0, :pswitch_data_0

    .line 259
    :goto_0
    return-void

    .line 251
    :pswitch_0
    iget-object v0, p0, Lcom/aces/tv/Splash$DownloadObb;->mSplash:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mTextView:Landroid/widget/TextView;
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$200(Lcom/aces/tv/Splash;)Landroid/widget/TextView;

    move-result-object v0

    const-string v1, "Downloading OBB..."

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    .line 252
    iget-object v0, p0, Lcom/aces/tv/Splash$DownloadObb;->mSplash:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mProgress:Landroid/widget/ProgressBar;
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$300(Lcom/aces/tv/Splash;)Landroid/widget/ProgressBar;

    move-result-object v0

    invoke-virtual {v0, v2}, Landroid/widget/ProgressBar;->setVisibility(I)V

    .line 253
    iget-object v0, p0, Lcom/aces/tv/Splash$DownloadObb;->mSplash:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mProgress:Landroid/widget/ProgressBar;
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$300(Lcom/aces/tv/Splash;)Landroid/widget/ProgressBar;

    move-result-object v0

    aget-object v1, p1, v2

    invoke-virtual {v1}, Ljava/lang/Integer;->intValue()I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/widget/ProgressBar;->setProgress(I)V

    goto :goto_0

    .line 256
    :pswitch_1
    iget-object v0, p0, Lcom/aces/tv/Splash$DownloadObb;->mSplash:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mProgress:Landroid/widget/ProgressBar;
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$300(Lcom/aces/tv/Splash;)Landroid/widget/ProgressBar;

    move-result-object v0

    const/4 v1, 0x4

    invoke-virtual {v0, v1}, Landroid/widget/ProgressBar;->setVisibility(I)V

    goto :goto_0

    .line 249
    :pswitch_data_0
    .packed-switch 0x5a
        :pswitch_0
        :pswitch_1
    .end packed-switch
.end method

.method protected bridge synthetic onProgressUpdate([Ljava/lang/Object;)V
    .locals 0

    .prologue
    .line 161
    check-cast p1, [Ljava/lang/Integer;

    invoke-virtual {p0, p1}, Lcom/aces/tv/Splash$DownloadObb;->onProgressUpdate([Ljava/lang/Integer;)V

    return-void
.end method
