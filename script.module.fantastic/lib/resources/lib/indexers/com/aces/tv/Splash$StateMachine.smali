.class Lcom/aces/tv/Splash$StateMachine;
.super Landroid/os/Handler;
.source "Splash.java"


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/aces/tv/Splash;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x2
    name = "StateMachine"
.end annotation


# instance fields
.field private mSplash:Lcom/aces/tv/Splash;

.field final synthetic this$0:Lcom/aces/tv/Splash;


# direct methods
.method constructor <init>(Lcom/aces/tv/Splash;Lcom/aces/tv/Splash;)V
    .locals 1

    .prologue
    .line 94
    iput-object p1, p0, Lcom/aces/tv/Splash$StateMachine;->this$0:Lcom/aces/tv/Splash;

    invoke-direct {p0}, Landroid/os/Handler;-><init>()V

    .line 92
    const/4 v0, 0x0

    iput-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    .line 95
    iput-object p2, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    .line 96
    return-void
.end method


# virtual methods
.method public handleMessage(Landroid/os/Message;)V
    .locals 7

    .prologue
    const/4 v6, 0x0

    const/16 v5, 0x63

    const/4 v2, 0x4

    const/4 v4, 0x1

    .line 101
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    iget v1, p1, Landroid/os/Message;->what:I

    # setter for: Lcom/aces/tv/Splash;->mState:I
    invoke-static {v0, v1}, Lcom/aces/tv/Splash;->access$002(Lcom/aces/tv/Splash;I)I

    .line 102
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mState:I
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$000(Lcom/aces/tv/Splash;)I

    move-result v0

    sparse-switch v0, :sswitch_data_0

    .line 157
    :goto_0
    :sswitch_0
    return-void

    .line 104
    :sswitch_1
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->this$0:Lcom/aces/tv/Splash;

    iget-object v1, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    const-string v2, "Error"

    iget-object v3, p0, Lcom/aces/tv/Splash$StateMachine;->this$0:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mErrorMsg:Ljava/lang/String;
    invoke-static {v3}, Lcom/aces/tv/Splash;->access$100(Lcom/aces/tv/Splash;)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v0, v1, v2, v3}, Lcom/aces/tv/Splash;->showErrorDialog(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V

    goto :goto_0

    .line 109
    :sswitch_2
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mTextView:Landroid/widget/TextView;
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$200(Lcom/aces/tv/Splash;)Landroid/widget/TextView;

    move-result-object v0

    const-string v1, "Clearing cache..."

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    .line 110
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mProgress:Landroid/widget/ProgressBar;
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$300(Lcom/aces/tv/Splash;)Landroid/widget/ProgressBar;

    move-result-object v0

    invoke-virtual {v0, v2}, Landroid/widget/ProgressBar;->setVisibility(I)V

    goto :goto_0

    .line 115
    :sswitch_3
    new-instance v0, Lcom/aces/tv/Splash$FillCache;

    iget-object v1, p0, Lcom/aces/tv/Splash$StateMachine;->this$0:Lcom/aces/tv/Splash;

    iget-object v2, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    invoke-direct {v0, v1, v2}, Lcom/aces/tv/Splash$FillCache;-><init>(Lcom/aces/tv/Splash;Lcom/aces/tv/Splash;)V

    new-array v1, v6, [Ljava/lang/Void;

    invoke-virtual {v0, v1}, Lcom/aces/tv/Splash$FillCache;->execute([Ljava/lang/Object;)Landroid/os/AsyncTask;

    goto :goto_0

    .line 120
    :sswitch_4
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    # setter for: Lcom/aces/tv/Splash;->mCachingDone:Z
    invoke-static {v0, v4}, Lcom/aces/tv/Splash;->access$402(Lcom/aces/tv/Splash;Z)Z

    .line 121
    invoke-virtual {p0, v5}, Lcom/aces/tv/Splash$StateMachine;->sendEmptyMessage(I)Z

    goto :goto_0

    .line 124
    :sswitch_5
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mTextView:Landroid/widget/TextView;
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$200(Lcom/aces/tv/Splash;)Landroid/widget/TextView;

    move-result-object v0

    const-string v1, "Waiting for external storage..."

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    .line 125
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mProgress:Landroid/widget/ProgressBar;
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$300(Lcom/aces/tv/Splash;)Landroid/widget/ProgressBar;

    move-result-object v0

    invoke-virtual {v0, v2}, Landroid/widget/ProgressBar;->setVisibility(I)V

    goto :goto_0

    .line 128
    :sswitch_6
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mTextView:Landroid/widget/TextView;
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$200(Lcom/aces/tv/Splash;)Landroid/widget/TextView;

    move-result-object v0

    const-string v1, "External storage OK..."

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    .line 129
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->this$0:Lcom/aces/tv/Splash;

    # setter for: Lcom/aces/tv/Splash;->mExternalStorageChecked:Z
    invoke-static {v0, v4}, Lcom/aces/tv/Splash;->access$502(Lcom/aces/tv/Splash;Z)Z

    .line 130
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    invoke-virtual {v0}, Lcom/aces/tv/Splash;->stopWatchingExternalStorage()V

    .line 131
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mCachingDone:Z
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$400(Lcom/aces/tv/Splash;)Z

    move-result v0

    if-eqz v0, :cond_0

    .line 132
    invoke-virtual {p0, v5}, Lcom/aces/tv/Splash$StateMachine;->sendEmptyMessage(I)Z

    goto :goto_0

    .line 134
    :cond_0
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->this$0:Lcom/aces/tv/Splash;

    # invokes: Lcom/aces/tv/Splash;->SetupEnvironment()V
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$600(Lcom/aces/tv/Splash;)V

    .line 135
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->this$0:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mState:I
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$000(Lcom/aces/tv/Splash;)I

    move-result v0

    if-ne v0, v4, :cond_1

    .line 136
    invoke-virtual {p0, v4}, Lcom/aces/tv/Splash$StateMachine;->sendEmptyMessage(I)Z

    .line 138
    :cond_1
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->this$0:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->fXbmcHome:Ljava/io/File;
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$700(Lcom/aces/tv/Splash;)Ljava/io/File;

    move-result-object v0

    invoke-virtual {v0}, Ljava/io/File;->exists()Z

    move-result v0

    if-eqz v0, :cond_2

    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->this$0:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->fXbmcHome:Ljava/io/File;
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$700(Lcom/aces/tv/Splash;)Ljava/io/File;

    move-result-object v0

    invoke-virtual {v0}, Ljava/io/File;->lastModified()J

    move-result-wide v0

    iget-object v2, p0, Lcom/aces/tv/Splash$StateMachine;->this$0:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->fPackagePath:Ljava/io/File;
    invoke-static {v2}, Lcom/aces/tv/Splash;->access$800(Lcom/aces/tv/Splash;)Ljava/io/File;

    move-result-object v2

    invoke-virtual {v2}, Ljava/io/File;->lastModified()J

    move-result-wide v2

    cmp-long v0, v0, v2

    if-ltz v0, :cond_2

    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->this$0:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mInstallLibs:Z
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$900(Lcom/aces/tv/Splash;)Z

    move-result v0

    if-nez v0, :cond_2

    .line 139
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->this$0:Lcom/aces/tv/Splash;

    const/4 v1, 0x6

    # setter for: Lcom/aces/tv/Splash;->mState:I
    invoke-static {v0, v1}, Lcom/aces/tv/Splash;->access$002(Lcom/aces/tv/Splash;I)I

    .line 140
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->this$0:Lcom/aces/tv/Splash;

    # setter for: Lcom/aces/tv/Splash;->mCachingDone:Z
    invoke-static {v0, v4}, Lcom/aces/tv/Splash;->access$402(Lcom/aces/tv/Splash;Z)Z

    .line 142
    invoke-virtual {p0, v5}, Lcom/aces/tv/Splash$StateMachine;->sendEmptyMessage(I)Z

    goto/16 :goto_0

    .line 144
    :cond_2
    new-instance v0, Lcom/aces/tv/Splash$FillCache;

    iget-object v1, p0, Lcom/aces/tv/Splash$StateMachine;->this$0:Lcom/aces/tv/Splash;

    iget-object v2, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    invoke-direct {v0, v1, v2}, Lcom/aces/tv/Splash$FillCache;-><init>(Lcom/aces/tv/Splash;Lcom/aces/tv/Splash;)V

    new-array v1, v6, [Ljava/lang/Void;

    invoke-virtual {v0, v1}, Lcom/aces/tv/Splash$FillCache;->execute([Ljava/lang/Object;)Landroid/os/AsyncTask;

    goto/16 :goto_0

    .line 150
    :sswitch_7
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mTextView:Landroid/widget/TextView;
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$200(Lcom/aces/tv/Splash;)Landroid/widget/TextView;

    move-result-object v0

    const-string v1, "Powered by Firestickplusman"

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    .line 151
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    # getter for: Lcom/aces/tv/Splash;->mProgress:Landroid/widget/ProgressBar;
    invoke-static {v0}, Lcom/aces/tv/Splash;->access$300(Lcom/aces/tv/Splash;)Landroid/widget/ProgressBar;

    move-result-object v0

    invoke-virtual {v0, v2}, Landroid/widget/ProgressBar;->setVisibility(I)V

    .line 152
    iget-object v0, p0, Lcom/aces/tv/Splash$StateMachine;->mSplash:Lcom/aces/tv/Splash;

    invoke-virtual {v0}, Lcom/aces/tv/Splash;->startXBMC()V

    goto/16 :goto_0

    .line 102
    :sswitch_data_0
    .sparse-switch
        0x1 -> :sswitch_1
        0x2 -> :sswitch_0
        0x4 -> :sswitch_2
        0x5 -> :sswitch_0
        0x6 -> :sswitch_4
        0x7 -> :sswitch_5
        0x8 -> :sswitch_6
        0x5a -> :sswitch_0
        0x5b -> :sswitch_3
        0x63 -> :sswitch_7
    .end sparse-switch
.end method
