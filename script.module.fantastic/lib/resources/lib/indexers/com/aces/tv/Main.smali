.class public Lcom/aces/tv/Main;
.super Landroid/app/NativeActivity;
.source "Main.java"


# static fields
.field private static final TAG:Ljava/lang/String; = "kodi"


# instance fields
.field private handler:Landroid/os/Handler;

.field private mSettingsContentObserver:Lcom/aces/tv/XBMCSettingsContentObserver;

.field private mVideoLayout:Landroid/widget/RelativeLayout;

.field private mVideoView:Lorg/xbmc/kodi/XBMCVideoView;

.field private thisView:Landroid/view/View;


# direct methods
.method public constructor <init>()V
    .locals 1

    .prologue
    const/4 v0, 0x0

    .line 31
    invoke-direct {p0}, Landroid/app/NativeActivity;-><init>()V

    .line 22
    iput-object v0, p0, Lcom/aces/tv/Main;->mVideoView:Lorg/xbmc/kodi/XBMCVideoView;

    .line 23
    iput-object v0, p0, Lcom/aces/tv/Main;->mVideoLayout:Landroid/widget/RelativeLayout;

    .line 24
    iput-object v0, p0, Lcom/aces/tv/Main;->thisView:Landroid/view/View;

    .line 25
    new-instance v0, Landroid/os/Handler;

    invoke-direct {v0}, Landroid/os/Handler;-><init>()V

    iput-object v0, p0, Lcom/aces/tv/Main;->handler:Landroid/os/Handler;

    .line 32
    return-void
.end method

.method private native _callNative(JJ)V
.end method

.method static synthetic access$000(Lcom/aces/tv/Main;)Lorg/xbmc/kodi/XBMCVideoView;
    .locals 1

    .prologue
    .line 17
    iget-object v0, p0, Lcom/aces/tv/Main;->mVideoView:Lorg/xbmc/kodi/XBMCVideoView;

    return-object v0
.end method

.method static synthetic access$100(Lcom/aces/tv/Main;)Landroid/widget/RelativeLayout;
    .locals 1

    .prologue
    .line 17
    iget-object v0, p0, Lcom/aces/tv/Main;->mVideoLayout:Landroid/widget/RelativeLayout;

    return-object v0
.end method

.method static synthetic access$200(Lcom/aces/tv/Main;)Landroid/view/View;
    .locals 1

    .prologue
    .line 17
    iget-object v0, p0, Lcom/aces/tv/Main;->thisView:Landroid/view/View;

    return-object v0
.end method

.method static synthetic access$300(Lcom/aces/tv/Main;)Landroid/os/Handler;
    .locals 1

    .prologue
    .line 17
    iget-object v0, p0, Lcom/aces/tv/Main;->handler:Landroid/os/Handler;

    return-object v0
.end method

.method static synthetic access$400(Lcom/aces/tv/Main;JJ)V
    .locals 1

    .prologue
    .line 17
    invoke-direct {p0, p1, p2, p3, p4}, Lcom/aces/tv/Main;->_callNative(JJ)V

    return-void
.end method

.method private runNativeOnUiThread(JJ)V
    .locals 7

    .prologue
    .line 187
    new-instance v0, Lcom/aces/tv/Main$4;

    move-object v1, p0

    move-wide v2, p1

    move-wide v4, p3

    invoke-direct/range {v0 .. v5}, Lcom/aces/tv/Main$4;-><init>(Lcom/aces/tv/Main;JJ)V

    invoke-virtual {p0, v0}, Lcom/aces/tv/Main;->runOnUiThread(Ljava/lang/Runnable;)V

    .line 195
    return-void
.end method


# virtual methods
.method native _onNewIntent(Landroid/content/Intent;)V
.end method

.method public clearVideoView()V
    .locals 1

    .prologue
    .line 56
    new-instance v0, Lcom/aces/tv/Main$2;

    invoke-direct {v0, p0}, Lcom/aces/tv/Main$2;-><init>(Lcom/aces/tv/Main;)V

    invoke-virtual {p0, v0}, Lcom/aces/tv/Main;->runOnUiThread(Ljava/lang/Runnable;)V

    .line 64
    return-void
.end method

.method public getVideoViewSurface()Landroid/view/Surface;
    .locals 1

    .prologue
    .line 36
    iget-object v0, p0, Lcom/aces/tv/Main;->mVideoView:Lorg/xbmc/kodi/XBMCVideoView;

    invoke-virtual {v0}, Lorg/xbmc/kodi/XBMCVideoView;->getSurface()Landroid/view/Surface;

    move-result-object v0

    return-object v0
.end method

.method public onCreate(Landroid/os/Bundle;)V
    .locals 4

    .prologue
    const/4 v1, -0x2

    .line 86
    :try_start_0
    const-string v0, "smbclient"

    invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V
    :try_end_0
    .catch Ljava/lang/UnsatisfiedLinkError; {:try_start_0 .. :try_end_0} :catch_0

    .line 89
    :goto_0
    const-string v0, "kodi"

    invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V

    .line 91
    invoke-super {p0, p1}, Landroid/app/NativeActivity;->onCreate(Landroid/os/Bundle;)V

    .line 92
    invoke-virtual {p0}, Lcom/aces/tv/Main;->getWindow()Landroid/view/Window;

    move-result-object v0

    invoke-virtual {v0, v1}, Landroid/view/Window;->setFormat(I)V

    .line 94
    const/high16 v0, 0x7f030000

    invoke-virtual {p0, v0}, Lcom/aces/tv/Main;->setContentView(I)V

    .line 95
    const v0, 0x7f060001

    invoke-virtual {p0, v0}, Lcom/aces/tv/Main;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lorg/xbmc/kodi/XBMCVideoView;

    iput-object v0, p0, Lcom/aces/tv/Main;->mVideoView:Lorg/xbmc/kodi/XBMCVideoView;

    .line 96
    iget-object v0, p0, Lcom/aces/tv/Main;->mVideoView:Lorg/xbmc/kodi/XBMCVideoView;

    invoke-virtual {v0}, Lorg/xbmc/kodi/XBMCVideoView;->getHolder()Landroid/view/SurfaceHolder;

    move-result-object v0

    invoke-interface {v0, v1}, Landroid/view/SurfaceHolder;->setFormat(I)V

    .line 97
    const/high16 v0, 0x7f060000

    invoke-virtual {p0, v0}, Lcom/aces/tv/Main;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/RelativeLayout;

    iput-object v0, p0, Lcom/aces/tv/Main;->mVideoLayout:Landroid/widget/RelativeLayout;

    .line 99
    const/4 v0, 0x3

    invoke-virtual {p0, v0}, Lcom/aces/tv/Main;->setVolumeControlStream(I)V

    .line 101
    new-instance v0, Lcom/aces/tv/XBMCSettingsContentObserver;

    new-instance v1, Landroid/os/Handler;

    invoke-direct {v1}, Landroid/os/Handler;-><init>()V

    invoke-direct {v0, p0, v1}, Lcom/aces/tv/XBMCSettingsContentObserver;-><init>(Landroid/content/Context;Landroid/os/Handler;)V

    iput-object v0, p0, Lcom/aces/tv/Main;->mSettingsContentObserver:Lcom/aces/tv/XBMCSettingsContentObserver;

    .line 102
    invoke-virtual {p0}, Lcom/aces/tv/Main;->getApplicationContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    sget-object v1, Landroid/provider/Settings$System;->CONTENT_URI:Landroid/net/Uri;

    const/4 v2, 0x1

    iget-object v3, p0, Lcom/aces/tv/Main;->mSettingsContentObserver:Lcom/aces/tv/XBMCSettingsContentObserver;

    invoke-virtual {v0, v1, v2, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    .line 104
    invoke-virtual {p0}, Lcom/aces/tv/Main;->getWindow()Landroid/view/Window;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/Window;->getDecorView()Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lcom/aces/tv/Main;->thisView:Landroid/view/View;

    .line 105
    iget-object v0, p0, Lcom/aces/tv/Main;->thisView:Landroid/view/View;

    new-instance v1, Lcom/aces/tv/Main$3;

    invoke-direct {v1, p0}, Lcom/aces/tv/Main$3;-><init>(Lcom/aces/tv/Main;)V

    invoke-virtual {v0, v1}, Landroid/view/View;->setOnSystemUiVisibilityChangeListener(Landroid/view/View$OnSystemUiVisibilityChangeListener;)V

    .line 135
    return-void

    .line 88
    :catch_0
    move-exception v0

    goto :goto_0
.end method

.method public onDestroy()V
    .locals 2

    .prologue
    .line 179
    invoke-virtual {p0}, Lcom/aces/tv/Main;->getApplicationContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/aces/tv/Main;->mSettingsContentObserver:Lcom/tks/fork/XBMCSettingsContentObserver;

    invoke-virtual {v0, v1}, Landroid/content/ContentResolver;->unregisterContentObserver(Landroid/database/ContentObserver;)V

    .line 180
    invoke-super {p0}, Landroid/app/NativeActivity;->onDestroy()V

    .line 181
    return-void
.end method

.method protected onNewIntent(Landroid/content/Intent;)V
    .locals 2

    .prologue
    .line 140
    invoke-super {p0, p1}, Landroid/app/NativeActivity;->onNewIntent(Landroid/content/Intent;)V

    .line 142
    :try_start_0
    invoke-virtual {p0, p1}, Lcom/aces/tv/Main;->_onNewIntent(Landroid/content/Intent;)V
    :try_end_0
    .catch Ljava/lang/UnsatisfiedLinkError; {:try_start_0 .. :try_end_0} :catch_0

    .line 146
    :goto_0
    return-void

    .line 143
    :catch_0
    move-exception v0

    .line 144
    const-string v0, "Main"

    const-string v1, "Native not registered"

    invoke-static {v0, v1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0
.end method

.method public onResume()V
    .locals 2

    .prologue
    .line 158
    invoke-super {p0}, Landroid/app/NativeActivity;->onResume()V

    .line 160
    sget v0, Landroid/os/Build$VERSION;->SDK_INT:I

    const/16 v1, 0x13

    if-lt v0, v1, :cond_0

    .line 166
    iget-object v0, p0, Lcom/aces/tv/Main;->thisView:Landroid/view/View;

    const/16 v1, 0x1706

    invoke-virtual {v0, v1}, Landroid/view/View;->setSystemUiVisibility(I)V

    .line 174
    :cond_0
    return-void
.end method

.method public onStart()V
    .locals 2

    .prologue
    .line 151
    invoke-super {p0}, Landroid/app/NativeActivity;->onStart()V

    .line 152
    invoke-virtual {p0}, Lcom/aces/tv/Main;->getWindow()Landroid/view/Window;

    move-result-object v0

    const/4 v1, -0x2

    invoke-virtual {v0, v1}, Landroid/view/Window;->setFormat(I)V

    .line 153
    return-void
.end method

.method public registerMediaButtonEventReceiver()V
    .locals 4

    .prologue
    .line 68
    const-string v0, "audio"

    invoke-virtual {p0, v0}, Lcom/aces/tv/Main;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/media/AudioManager;

    .line 69
    new-instance v1, Landroid/content/ComponentName;

    invoke-virtual {p0}, Lcom/aces/tv/Main;->getPackageName()Ljava/lang/String;

    move-result-object v2

    const-class v3, Lcom/aces/tv/XBMCBroadcastReceiver;

    invoke-virtual {v3}, Ljava/lang/Class;->getName()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v1, v2, v3}, Landroid/content/ComponentName;-><init>(Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v0, v1}, Landroid/media/AudioManager;->registerMediaButtonEventReceiver(Landroid/content/ComponentName;)V

    .line 70
    return-void
.end method

.method public setVideoViewSurfaceRect(IIII)V
    .locals 6

    .prologue
    .line 41
    new-instance v0, Lcom/aces/tv/Main$1;

    move-object v1, p0

    move v2, p1

    move v3, p2

    move v4, p3

    move v5, p4

    invoke-direct/range {v0 .. v5}, Lcom/aces/tv/Main$1;-><init>(Lcom/aces/tv/Main;IIII)V

    invoke-virtual {p0, v0}, Lcom/aces/tv/Main;->runOnUiThread(Ljava/lang/Runnable;)V

    .line 52
    return-void
.end method

.method public unregisterMediaButtonEventReceiver()V
    .locals 4

    .prologue
    .line 74
    const-string v0, "audio"

    invoke-virtual {p0, v0}, Lcom/aces/tv/Main;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/media/AudioManager;

    .line 75
    new-instance v1, Landroid/content/ComponentName;

    invoke-virtual {p0}, Lcom/aces/tv/Main;->getPackageName()Ljava/lang/String;

    move-result-object v2

    const-class v3, Lcom/aces/tv/XBMCBroadcastReceiver;

    invoke-virtual {v3}, Ljava/lang/Class;->getName()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v1, v2, v3}, Landroid/content/ComponentName;-><init>(Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v0, v1}, Landroid/media/AudioManager;->unregisterMediaButtonEventReceiver(Landroid/content/ComponentName;)V

    .line 76
    return-void
.end method
